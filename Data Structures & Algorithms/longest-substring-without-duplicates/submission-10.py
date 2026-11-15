class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # take example [abcabcbb]
        maxSubString = 0
        leftPointer = 0
        characterIndexTracker = {}

        for index, char in enumerate(s):
            if char in characterIndexTracker:
                lastCharIndex = characterIndexTracker[char]
                leftPointer = max(leftPointer, lastCharIndex + 1)
            
            latestSubString = (index + 1) - leftPointer
            maxSubString = max(maxSubString, latestSubString)
            characterIndexTracker[char] = index
        
        return maxSubString

