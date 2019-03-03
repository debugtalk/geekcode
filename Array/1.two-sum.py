#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (41.97%)
# Total Accepted:    1.5M
# Total Submissions: 3.6M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#

class Solution:
    def twoSum(self, nums, target):

        list_mapping = {}

        for index, x in enumerate(nums):
            y = target -x
            if y in list_mapping:
                return [list_mapping[target - x], index]

            list_mapping[x] = index

        return [-1, -1]


# testcases
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(
            self.s.twoSum(nums, target),
            [0, 1]
        )

    def test_2(self):
        nums = [3,2,4]
        target = 6
        self.assertEqual(
            self.s.twoSum(nums, target),
            [1, 2]
        )

    def test_3(self):
        nums = [3,3]
        target = 6
        self.assertEqual(
            self.s.twoSum(nums, target),
            [0, 1]
        )


if __name__ == "__main__":
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    testcase = loader.loadTestsFromTestCase(TestSolution)
    runner.run(testcase)
