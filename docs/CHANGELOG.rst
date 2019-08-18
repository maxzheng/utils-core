Version 0.1.2
================================================================================

* Allow exception class to be changed for timeout and use SystemExit for processify
  
  SystemExit will ensure everything are terminated, while other exceptions may be caught and not handled
  properly (even another BaseException)

Version 0.1.1
--------------------------------------------------------------------------------

* Add timeout function and support to processify
* Test pickle of processify

Version 0.1.0
--------------------------------------------------------------------------------

* Rename package namespace from utils to utils_core to avoid conflicts with local utils.py packages.
  
  All imports should migrate to use utils_core, but the old namespace is maintained for backward compatibility.
* Add is_running to check if process is running
* Add processify to run function in a subprocess

Version 0.0.5
--------------------------------------------------------------------------------

* Add run_sync to run sync func in async program

Version 0.0.4
--------------------------------------------------------------------------------

* Support Python 3.7
* Ensure count is an int
* Add TimeUnit and plural

Version 0.0.3
--------------------------------------------------------------------------------

* Add links/contact info
* Ignore textcov and add missing import

Version 0.0.2
--------------------------------------------------------------------------------

* Initial commit
* Initial commit
