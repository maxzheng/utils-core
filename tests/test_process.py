import pytest

from utils.process import run, silent_run, RunError
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
