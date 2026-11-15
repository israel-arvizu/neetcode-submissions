class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # have a variable holding the max substring
        maxSubString = 0
        leftPointer = 0
        # hold the latest index of each char
        characterTracker = {}
        # go through the list
        for index, char in enumerate(s):
            # check the dict if it already exists
            if char in characterTracker:
                # if it does exist, check its last location
                lastIndex = characterTracker.get(char)
                leftPointer = max(leftPointer, lastIndex + 1)
            # update the dict value index to the latest
            characterTracker[char] = index
            subStringLength = index - leftPointer + 1
            maxSubString = max(maxSubString, subStringLength)

        return maxSubString
