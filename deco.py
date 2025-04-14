#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import sys


def factorial(n: int) -> int:
    if n < 2:
        return n
    else:
        return factorial(n - 1) * n


if __name__ == "__main__":
    n: int = int(sys.argv[1])
    print(factorial(n))
