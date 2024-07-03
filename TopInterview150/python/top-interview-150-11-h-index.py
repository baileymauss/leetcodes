"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        if citations[-1] == 0:
            return 0
        for i in range(n):
            if citations[i] >= n - i:
                return (n - i)