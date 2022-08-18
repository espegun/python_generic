# How to threading

[Intro to Python Threading @ RealPython](https://realpython.com/intro-to-python-threading/)  

Have a look at the explanation above. Instead of using the basic, underlying `threading` module which uses `t.start()` and `t.join()`, rather use `concurrent.futures.ThreadPoolExecutor` which handles a bunch of threads in parallell and wait for the last one to finish. See the example-file in this repo.
