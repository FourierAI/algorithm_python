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
    median = len(seq) //2
    left_seq = mergesort(seq[0:median])
    right_seq = mergesort(seq[median:])

    left_index = 0
    right_index = 0

    left_len = len(left_seq)
    right_len = len(right_seq)

    merge_seq = []
    while left_index<left_len and right_index<right_len:
        if left_seq[left_index]<=right_seq[right_index]:
            merge_seq.append(left_seq[left_index])
            left_index +=1
        else:
            merge_seq.append(right_seq[right_index])
            right_index +=1

    while left_index<left_len:
        merge_seq.append(left_seq[left_index])
        left_index +=1
    while right_index<right_len:
        merge_seq.append(right_seq[right_index])
        right_index +=1

    return merge_seq


if __name__== '__main__':

    test_seq = [1,32,41,2,1,42,12,43,123,53,2,5,62]

    # for index in range(len(test_seq)):
    #     j = index
    #     while test_seq[j-1] > test_seq[j] and j >=0:
    #         test_seq[j-1],test_seq[j] = test_seq[j],test_seq[j-1]
    #         j -= 1

    test_seq = mergesort(test_seq)
    print(test_seq)

