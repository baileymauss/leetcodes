"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # create hashmap to store previous elements
        hmap = {}

        # traverse all elements
        for i in range(len(nums)):
            # if duplicate is present and distance is less than or equal to k, return true
            if nums[i] in hmap and (i - hmap[nums[i]]) <= k:
                return True
            # update hashmap to contain new value
            hmap[nums[i]] = i
        return False