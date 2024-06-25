# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        # Reverse entire array
        self.reverse(nums, 0, n-1)

        # Reverse first k elements of array
        self.reverse(nums, 0, k - 1)

        # Reverse remaining n - k elements
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1