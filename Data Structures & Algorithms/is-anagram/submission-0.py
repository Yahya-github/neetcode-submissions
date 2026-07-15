class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = sorted(tuple(s))
        string2 = sorted(tuple(t))
        return string1 == string2