#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: combination.py
# @time: 2020-03-20 12:33
# @desc:

def combine(n, k):
    whole_list = [i for i in range(1,n+1)]

    result = []
    for i in range(len(whole_list)-k+1):
        for j in range(i+1,len(whole_list)-k+1):
            combine_list = [whole_list[i]]
            for m in range(j,j+k-1):
                combine_list.append(whole_list[m])
            result.append(combine_list)
    return result


combine(2,1)