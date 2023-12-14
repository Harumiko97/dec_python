import operator
from functools import wraps
import time
from functools import lru_cache

# Task 1


# Task 2
def log_info(information):
    @wraps(information)
    def wrapped(*args, **kwargs):
        print('log init value:', args[0])
        res = information(*args, **kwargs)
        print('log result:', res)
        return res
    return wrapped


@log_info
def function(a):
    return a + 10


print('Result:', function(10))

# Task 3

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        res = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args}{kwargs} Took {total_time}')
        return res
    return timeit_wrapper

@timeit
def math(num):
    total = sum((num for i in range(0, num ** 2)))
    return total

if __name__ == '__main__':
    math(10)
    math(20)
    math(30)


# Task 4
def rate_limits(max_calls, period):
    def decorator(func):
        calls = 0
        last_reset = time.time()

        def wrapper(*args, **kwargs):
            nonlocal calls, last_reset
            elapsed = time.time() - last_reset
            if elapsed > period:
                calls = 0
                last_reset = time.time()
            if calls >= max_calls:
                raise Exception('Rate limit exceeded.')
            calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator


@rate_limits(max_calls=3, period=5)
def api_call():
    print('API call success.')
    for _ in range(8):
        try:
            api_call()
        except Exception as e:
            print(f'Error: {e}')
            return api_call


# Task 5
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


print(([fib(n) for n in range(16)]))
print(fib.cache_info())
