"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_chars = {}
        t_vals = set()
        for i in range(len(s)):
            if s[i] in map_chars:
                if map_chars[s[i]] != t[i]:
                    return False
            else:
                if t[i] in t_vals:
                    return False
                map_chars[s[i]] = t[i]
                t_vals.add(t[i])
        return True