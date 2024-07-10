"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # dictionary to map pattern characters to words
        char_to_word = {}

        # dictionary to map words to pattern characters
        word_to_char = {}

        # split string of words into list of words
        words = s.split()

        if len(pattern) != len(words):
            return False
            
        # iterate through each pattern character and corresponding word
        for i in range(len(pattern)):
            current_char = pattern[i]
            current_word = words[i]

            # if the current character and word aren't mapped yet, add them
            if current_char not in char_to_word and current_word not in word_to_char:
                char_to_word[current_char] = current_word
                word_to_char[current_word] = current_char
            else:
                # if current character or word already exists in dictionaries, check if the key-value is consistent
                if char_to_word.get(current_char) != current_word or word_to_char.get(current_word) != current_char:
                    return False
        return True