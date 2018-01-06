#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def myTrim(s):
    ss = ''
    for i in range(len(s)):
        if cmp(s[i],' ') == 0 :
            continue
        else:
            ss = ss + s[i]
    return ss;


print(myTrim("  oajkdfiog wf  "))


