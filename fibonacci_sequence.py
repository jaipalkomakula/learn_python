#!/usr/bin/env python

## Fibonacci sequence - example 
i,j = 0,1
for i in xrange(1,5):
    print i
    i,j = j,i+j
