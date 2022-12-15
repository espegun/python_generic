# Logging in Python
* For the most basic example, see `logging_demo.py`. It uses the `logging.basicConfig` setup, which is simple and preferable if sufficient.
* For parallell threads logging to different files, see `parallell_logs.py`. It creates separate `logger` objects.
* `logger` objects should only be created by the `logging.getLogger` function
* `logger` objects has handler objects, typically `FileHandler` which directs the logs to certains files.
* `FileHandler` objects has `logging.Formatter`

Note that it by design is difficult to remove `logger` objects, so rather reuse/redirect that creating many of them.

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
