#!/usr/bin/env python
# encoding: utf-8

# @author: Zhipeng Ye
# @contact: Zhipeng.ye19@xjtlu.edu.cn
# @file: treenode.py
# @time: 2020-02-25 23:42
# @desc:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):

        if nums == None:
            return None

        nums_length = len(nums)
        if nums_length == 0:
            return None

        median_index = nums_length // 2

        node = TreeNode(nums[median_index])

        node.left = self.sortedArrayToBST(nums[:median_index])
        node.right = self.sortedArrayToBST(nums[median_index+1:])

        return node

if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    sol = Solution()
    node = sol.sortedArrayToBST(nums)
    print(node)