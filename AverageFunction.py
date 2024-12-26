#!/bin/python

import math
import os
import random
import re
import sys


# write your code here
def avg(*n):
    return sum(n)*1.0/len(n) 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = map(int, raw_input().split())
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
