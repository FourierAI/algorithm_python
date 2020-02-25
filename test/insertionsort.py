#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: insertionsort.py
# @time: 2020-02-24 21:41
# @desc:

def mergesort(seq):
    if len(seq) == 1:
        return seq




if __name__== '__main__':

    test_seq = [1,32,41,2,1,42,12,43,123,53,2,5,62]

    for index in range(len(test_seq)):
        j = index
        while test_seq[j-1] > test_seq[j] and j >=0:
            test_seq[j-1],test_seq[j] = test_seq[j],test_seq[j-1]
            j -= 1

    print(test_seq)

