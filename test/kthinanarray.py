#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: kthinanarray.py
# @time: 2020-02-18 15:42
# @desc:

def findKthLargest( nums, k):
    return findKthSmallest(nums,len(nums)-k+1)

def findKthSmallest( nums, k):
    nums_length = len(nums)

    i = 0
    j = nums_length - 1
    key = nums[0]
    while (i != j):
        while i< j and nums[j] > key:
            j -=1
        nums[i], nums[j] = nums[j], nums[i]
        while i<j and nums[i] < key:
            i +=1
        nums[j], nums[i] = nums[i], nums[j]
    current_position = i

    if k == current_position + 1:
        return nums[current_position]
    elif k < current_position + 1:
        return findKthSmallest(nums[:current_position], k)
    else:
        return findKthSmallest(nums[current_position + 1:], k - current_position - 1)

if __name__ == '__main__':

    print(findKthLargest([5,2,4,1,3,6,0],4))