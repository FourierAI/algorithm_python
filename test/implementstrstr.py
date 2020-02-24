#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: implementstrstr.py
# @time: 2020-02-22 16:27
# @desc:



class Solution:
    def strStr(self, haystack, needle):

        if len(needle) == 0:
            return 0


        haystack_length = len(haystack)

        needle_length = len(needle)

        if needle_length > haystack_length:
            return -1

        index= -1
        for i in range(haystack_length):

            j=0
            current_i = i
            while current_i < haystack_length and haystack[current_i] == needle[j]:
                current_i +=1
                j +=1

                if j>=needle_length:
                    return current_i - needle_length+1

        return index


if __name__ == '__main__':
    solution = Solution()

    print(solution.strStr('mississippi','issipi'))