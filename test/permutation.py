#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: permutation.py
# @time: 2020-03-18 22:46
# @desc:
def permute(nums):
    paths = []

    def record_path(path,nums_copy):
        if len(nums_copy) ==1:
            path.append(nums_copy[0])
            paths.append(path)
            return

        for i in range(len(nums_copy)):
            path = path[:]
            path.append(nums_copy[i])
            nums_copy_copy = nums_copy[:]
            del(nums_copy_copy[i])
            record_path(path,nums_copy_copy)

    record_path([],nums)

    print(paths)

permute([1,2,3])