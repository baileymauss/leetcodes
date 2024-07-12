"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map to store value, index already checked
        prev_map = {}

        # iterate over list
        for i, n in enumerate(nums):
            # calculate what value needs to exist for the current list value to be the solution
            diff = target - n
            # if that value appears in the hashmap, that value's index and the current list index is the solution
            if diff in prev_map:
                return [prev_map[diff], i]
            # update hashmap to reflect value, index already checked
            prev_map[n] = i