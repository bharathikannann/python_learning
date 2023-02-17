# Decortors can be applied to functions, methods, classes and even modules
# Usage: @decorator_name or @decorator_name(args) or @decorator_name(args, kwargs) before the function definition
# Decorators can be chained together, e.g. @decorator1 @decorator2 @decorator3
# Useful links: https://towardsdatascience.com/5-real-handy-python-decorators-for-analyzing-debugging-your-code-c22067318d47

# Available decorators:
#   - timeit
#   - performance_check
#   - repeater
#   - cache
#   - prompt_sure

import time
from functools import wraps

# ----------------- Timeit decorator -----------------

# Decorator to measure the time taken by a function
def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

# ----------------- Performance check decorator -----------------

import tracemalloc
# Decorator to measure the memory usage of a function
def performance_check(func):
    """Measure performance of a function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
      tracemalloc.start()
      start_time = time.perf_counter()
      res = func(*args, **kwargs)
      duration = time.perf_counter() - start_time
      current, peak = tracemalloc.get_traced_memory()
      tracemalloc.stop()

      print(f"\nFunction:             {func.__name__} ({func.__doc__})"
            f"\nMemory usage:         {current / 10**6:.6f} MB"
            f"\nPeak memory usage:    {peak / 10**6:.6f} MB"
            f"\nDuration:             {duration:.6f} sec"
            f"\n{'-'*40}"
      )
      return res
    return wrapper

# ----------------- Repeater decorator -----------------
    
# Decorator to repeat a function 
def repeater(iterations:int=1):
  """ Repeats the decorated function [iterations] times """

  def outer_wrapper(func):
    def wrapper(*args, **kwargs):
      res = None
      for i in range(iterations):
        res = func(*args, **kwargs)
      return res
    return wrapper
  return outer_wrapper

# ----------------- Cache decorator -----------------

# Decorator to cache the result of a function
def cache(func):
    """Caches the result of a function"""
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

# ----------------- Prompt sure decorator -----------------

# Decorator to prompt the user before executing a function
def prompt_sure(prompt_text:str):
  """ Shows prompt asking you whether you want to continue. Exits on anything but y(es) """

  def outer_wrapper(func):
    def wrapper(*args, **kwargs):
      if (input(prompt_text).lower() != 'y'):
        return
      return func(*args, **kwargs)
    return wrapper
  return outer_wrapper