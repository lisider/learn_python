#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a=0
b=0
try:
    c = b/ a
    print(c)
except (IOError ,ZeroDivisionError),x:
    print(x)
else:
    print("no error")
print("done")

