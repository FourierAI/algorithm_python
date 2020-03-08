#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: validparentheses.py
# @time: 2020-03-08 13:32
# @desc:

class Solution:
    def isValid(self, s):

        vector = []

        for char in s:
            if len(vector) == 0 or vector[-1] != char:
                vector.append(char)
                continue

            if len(vector) > 0 and vector[-1] == char:
                vector.pop()

        return len(vector) == 0

if __name__ == "__main__":

    test = '()'

    Solution().isValid(test)