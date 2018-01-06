#!/usr/bin/env python3
# -*- coding: utf-8 -*-
L = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', 'Ruby', 'PHP'],
        ['Adam', 'Bart', 'Lisa']
    ]

M = ('a','b','c')

P = (L,M)

print(L)
print(M)
print(P)

P[0][0][0] = 'POP'

print("-----------");

print(L)
print(M)
print(P)
