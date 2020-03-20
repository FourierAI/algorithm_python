#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: longest increasing sequence.py
# @time: 2020-03-18 17:21
# @desc:

def lengthOfLIS( nums):
    nums_length = len(nums)
    if nums_length == 0:
        return 0

    max_length = 1
    for i in range(nums_length-1):
        help_stack = [nums[i]]
        for j in range(i+1,nums_length):
            if nums[j]>help_stack[-1]:
                help_stack.append(nums[j])

        if len(help_stack) >max_length:
            max_length = len(help_stack)

    return max_length


print(lengthOfLIS([10,9,2,5,3,4]))

