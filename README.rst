utils-core
===========

General utilities on top of Python standard libraries.

Examples for process-related utilities:

.. code-block:: python

    from utils.process import run, silent_run


    run('ls -l')
    out = run(['ls', '-l'], return_output=True)

    # Just runs without any output to stdout. Alias for: run(..., silent=True)
    silent_run('ls -l')

Examples for filesystem-related utilities:

.. code-block:: python

    import os

    from utils.fs import in_dir, in_temp_dir


    with in_temp_dir() as tmpdir:
        assert os.getcwd() == tmpdir

    with in_dir('/tmp'):
        assert os.getcwd() == '/tmp'
