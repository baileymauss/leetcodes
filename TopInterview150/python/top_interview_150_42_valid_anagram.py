"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # create dict to count occurrences of a letter
        counter = {}
        # for every character in the first string,
        # if it does not already exist in the dict, add it and set value to zero
        # then increment its count value
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        # for every character in the second string,
        # if at any point we find its count is already at zero, return false
        # then decrement its count
        for char in t:
            if counter.get(char, 0) == 0:
                return False
            counter[char] -= 1
        # if all checks are failed, our dictionary should have exactly 0 counted for each letter
        # meaning each letter appears exactly the same number of times in each string
        return True
