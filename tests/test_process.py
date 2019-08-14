import os

import pytest

from utils.process import run, silent_run, RunError, processify, is_running
from utils.fs import in_temp_dir


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


def test_processify():
    @processify
    def test_function():
        return os.getpid()

    @processify
    def test_deadlock():
        """ Ensure large results does not end in a deadlock """
        return range(30000)

    @processify
    def test_exception():
        raise RuntimeError('xyz')

    child_pid = test_function()
    assert os.getpid() != child_pid > 0
    assert not is_running(child_pid)
    assert len(test_deadlock()) == 30000

    with pytest.raises(RuntimeError) as e:
        test_exception()
    assert 'xyz' in str(e)


def test_is_running():
    assert is_running(os.getpid())
