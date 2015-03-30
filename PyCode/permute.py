#!/usr/bin/env python
# encoding: utf-8

def per(fst, lst):
    if len(lst) == 0:
        print fst
    else:
        for ele in lst:
            per(fst + [ele], [_ for _ in lst if _ not in [ele]])

def permute(inplist):
    per([], inplist)

permute([1,2,3,4])
