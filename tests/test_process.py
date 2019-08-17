import os
import pickle
import time

import pytest

from utils_core.process import run, silent_run, RunError, processify, is_running
from utils_core.fs import in_temp_dir


def test_run(capsys):
    with in_temp_dir():
        assert run('echo hello > hello.txt; echo world >> hello.txt', shell=True)

        out = run('ls', return_output=True)
        assert out == 'hello.txt\n'

        out = run(['cat', 'hello.txt'], return_output=True)
        assert out == 'hello\nworld\n'

        with pytest.raises(RunError):
            run('blah')

        assert not run('blah', raises=False)

        assert silent_run('ls -l')
        out, _ = capsys.readouterr()
        assert out == ''


@processify
def get_child_pid():
    return os.getpid()


def test_processify():
    child_pid = get_child_pid()
    assert os.getpid() != child_pid > 0
    assert not is_running(child_pid)

    get_pid = pickle.loads(pickle.dumps(get_child_pid))
    assert get_pid() > 0


def test_processify_deadlock():
    @processify
    def test_deadlock():
        """ Ensure large results does not end in a deadlock """
        return range(30000)

    assert len(test_deadlock()) == 30000


def test_processify_exception():
    @processify
    def test_exception():
        raise RuntimeError('xyz')

    with pytest.raises(RuntimeError) as e:
        test_exception()

    assert 'xyz' in str(e)


def test_processify_timeout():
    @processify(timeout=1)
    def test_timeout_happened():
        time.sleep(2)
        return "this never happens"

    with pytest.raises(TimeoutError) as e:
        test_timeout_happened()

    assert 'Timed out after 1 second' in str(e)

    @processify(timeout=1)
    def test_timeout_not():
        return "no timeout"

    assert 'no timeout' == test_timeout_not()


def test_is_running():
    assert is_running(os.getpid())
