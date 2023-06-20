#!/usr/bin/env python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    t = int(input().strip())
    total = 0
    numbers = []
    for i in range(1, t):
        if i % 3 == 0 or i % 5 == 0:
            total += i
            numbers.append(i)
    print("sum of the following {} is: {}".format(numbers, total))
