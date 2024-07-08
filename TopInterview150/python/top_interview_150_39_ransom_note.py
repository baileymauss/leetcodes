"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # python Counter class is a subclass of a dict
        # it creates a dict counting the occurrence of elements
        # eg. string 'aabc' -> [('a', 2), ('b', 1), ('c',1)]
        # comparing one Counter to another for this problem,
        # you could use st1 & st2 (bitwise and, or intersection)
        # or st1 <= st2 (is all of st1 included in st2)
        st1 = Counter(ransomNote)
        st2 = Counter(magazine)
        return st1 <= st2