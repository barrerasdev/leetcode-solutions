# Find the difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        charSet = {}

        for ch in s:
            charSet[ch] = charSet.get(ch, 0) + 1

        for ch in t:
            charSet[ch] = charSet.get(ch, 0) - 1
            if charSet[ch] < 0:
                return ch

        return ''

