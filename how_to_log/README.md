# Logging in Python

* For the most basic example, see `logging_demo.py`
* For parallell threads logging to different files, see `parallell_logs.py`

Five levels of severity in decreasing order:
* `logging.critical("Critical!")`
* `logging.error("Some error!")`
* `logging.warning("A warning...!")`
* `logging.info("Some info")`
* `logging.debug("Howdy!!")`
Every event from and above the `level` specified in `logging.basicConfig()` will be included in the log.

Sources:
* Howto: https://docs.python.org/3/howto/logging.html
* Cookbook: https://docs.python.org/3/howto/logging-cookbook.html
* *Python Cookbook, p555-559*
