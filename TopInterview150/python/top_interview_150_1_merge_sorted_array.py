"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # index1 tracks length of nums1, starting at m-1 and decrementing
        index1 = m-1
        # index2 tracks length of nums2, starting at n-1 and decrementing
        index2 = n-1
        # currentposition tracks the position we are currently placing the larger element in nums1
        currentposition = (m+n)-1

        # we iterate through all elements in nums2
        # if there are still elements in nums1 we do not need to iterate over them, as they are already correctly placed
        while index2 >= 0:
            # check if the value in nums1 is larger than the value in nums2
            if index1 >= 0 and nums1[index1] > nums2[index2]:
                # if it is, assign the current space in nums1 to the value in nums1
                nums1[currentposition] = nums1[index1]
                # decrement nums1 index
                index1 -= 1
            else:
                # otherwise, assign the current space in nums1 to the value in nums2
                nums1[currentposition] = nums2[index2]
                # decrement nums2 index
                index2 -= 1
            # after every iteration, decrement the current position in nums1
            currentposition -= 1