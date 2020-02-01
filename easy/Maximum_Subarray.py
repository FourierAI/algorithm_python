#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: Maximum_Subarray.py
# @time: 2019-11-28 15:30
# @desc:


class Solution:

    def maxSubArray(nums):
        max_sum = 0
        sum_value = 0
        for num in nums:

            sum_value = sum_value + num

            if sum_value < 0:
                sum_value = 0
                continue

            if sum_value >= max_sum:
                max_sum = sum_value

        return max_sum


if __name__ == '__main__':
    test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    max_sum = Solution.maxSubArray(test)

    print(max_sum)
