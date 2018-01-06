#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 0

b = range(10000)
for i in b:
    a = a + b[i]
    
print(a)
