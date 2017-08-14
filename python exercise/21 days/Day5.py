#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/14 19:40
# @Author  : Zhangyuanyuan
# @Site    : 
# @File    : Day5.py
# @Software: PyCharm Community Edition

#leetcode1
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self,nums,target):
        """

        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        print(nums)
        if len(nums)<=1:
            return False
        buff = {}
        for i in range(len(nums)):
            if nums[i] in buff:
                return [buff[nums[i]],i]
            else:
                buff[target - nums[i]] = i


if __name__ == "__main__":
    s = Solution()
    re = s.twoSum([2,7,13,15],9)
    print(re)