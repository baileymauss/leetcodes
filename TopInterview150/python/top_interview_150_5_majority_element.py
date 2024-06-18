"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # using boyer-moore majority voting algorithm
        votes = 0
        for i in range(len(nums)):
            if votes == 0:
                candidate = nums[i]
                votes = 1
            else:
                if nums[i] == candidate:
                    votes += 1
                else:
                    votes -= 1
        return candidate