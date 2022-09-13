# How to threading

[Intro to Python Threading @ RealPython](https://realpython.com/intro-to-python-threading/)  
[Threading in Python: The Complete Guide](https://superfastpython.com/threading-in-python/)  
[Run Code Concurrently Using the Threading Module](https://youtu.be/IEEhzQoKtQU)  
[ThreadPoolExecutor](https://superfastpython.com/threadpoolexecutor-in-python/)  
[Threads and Queue](https://medium.datadriveninvestor.com/the-most-simple-explanation-of-threads-and-queues-in-python-cbc206025dd1)  

* Think of it as two or more processes running in parallell, this is very often useful when processes are waiting for events (tests finished, user input).
* However, below the hood, Python threads are limited to actually run one at a time, even when running on different CPUs. If you wish to process using several CPUs at once, use the `multiprocessing` module.

## Threading basics
See the file 



## ThreadPoolExecutor

Have a look at the explanation above. Instead of using the basic, underlying `threading` module which uses `t.start()` and `t.join()`, rather use `concurrent.futures.ThreadPoolExecutor` which handles a bunch of threads in parallell and wait for the last one to finish. See the example-file in this repo.



## Queue - cross thread communication
...TBD..

