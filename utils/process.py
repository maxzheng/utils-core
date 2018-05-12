import logging
import subprocess
import sys

log = logging.getLogger(__name__)


class RunError(Exception):
    pass


def silent_run(*args, **kwargs):
    """ Same as run with slient=True """
    return run(*args, silent=True, **kwargs)


def run(cmd, cwd=None, silent=None, return_output=False, raises=True, **subprocess_args):
    """
    Runs a CLI command.

    :param list/str cmd: Command with args to run.
    :param str cwd: Change directory to cwd before running
    :param bool/int silent: Suppress stdout/stderr.
                            If True, completely silent.
                            If 2, print cmd output on error.
    :param bool return_output: Return the command output. Defaults silent=True. Set silent=False to see output.
                               If True, always return output.
                               If set to 2, return a tuple of (output, success) where output is the output of the
                               command and success is exit code 0.
                               When used, it is guaranteed to always return output / other options are ignored
                               (like raises).
    :param bool raises: Raise an exception if command exits with an error code.
    :param dict subprocess_args: Additional args to pass to subprocess
    :return: Output or boolean of success depending on option selected
    :raise RunError: if the command exits with an error code and raises=True
    """

    if isinstance(cmd, str):
        cmd = cmd.split()

    cmd_str = ' '.join(cmd)

    if 'shell' in subprocess_args and subprocess_args['shell']:
        cmd = cmd_str

    log.debug('Running: %s %s', cmd_str, '[%s]' % cwd if cwd else '')

    if return_output and silent is None:
        silent = True

    try:
        if silent or return_output:
            p = subprocess.Popen(cmd, cwd=cwd, bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                 **subprocess_args)
            exit_code = -1

            if silent:
                output, _ = p.communicate()
                exit_code = p.returncode
            else:
                output = ''
                ch = True
                while ch:
                    ch = p.stdout.read(1)
                    sys.stdout.write(ch)
                    sys.stdout.flush()
                    output += ch
                    if p.poll() is not None and exit_code == -1:
                        exit_code = p.returncode

            output = output.decode('utf-8')

            if return_output is True:
                return output
            elif return_output == 2:
                return output, exit_code == 0

            if exit_code == 0:
                if return_output:
                    return output
                else:
                    return True

            elif raises or silent == 2:
                if output and silent:
                    print(output.strip())

        else:
            exit_code = subprocess.call(cmd, cwd=cwd, **subprocess_args)
            if exit_code == 0:
                return True

    except Exception as e:
        if raises:
            log.debug(e, exc_info=True)
            raise RunError('Command "%s" could not be run because %s' % (cmd_str, e))

    # We only get here if exit code != 0
    if raises:
        raise RunError('Command "%s" returned non-zero exit status %d' % (cmd_str, exit_code))

    return False
