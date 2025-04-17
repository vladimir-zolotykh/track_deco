#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import sys
from functools import wraps
import time
import logging


count: int = 0
logging.basicConfig(level=logging.DEBUG)


def track(limit: int = 3):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kw):
            global count
            if count < limit:
                logging.info(f"{func.__name__} has called")
            count += 1
            # t1: float = time.perf_counter()
            res = func(*args, **kw)
            # t2: float = time.perf_counter()
            # if count < limit:
            #     logging.info(f"{func.__name__} took {t2 - t1} seconds")
            return res

        return wrapper

    return decorate


@track(5)
def factorial(n: int) -> int:
    if n < 2:
        return n
    else:
        return factorial(n - 1) * n


if __name__ == "__main__":
    n: int = int(sys.argv[1])
    print(factorial(n))
