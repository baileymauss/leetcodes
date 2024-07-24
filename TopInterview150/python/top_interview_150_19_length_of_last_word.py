"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        previous = ''
        word_length = 0
        for char in s:
            if char != ' ':
                if previous == ' ':
                    word_length = 0
                word_length += 1
            previous = char
        return word_length