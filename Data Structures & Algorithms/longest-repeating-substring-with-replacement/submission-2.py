class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # two pointers
        leftPointer = 0
        rightPointer = 0
        # count of chars
        charCount = defaultdict(int)
        maxSubSLength = 0

        # while right pointer is not end of the list
        while rightPointer < len(s):
            # add the current letter to the charCount
            currentChar = s[rightPointer]
            charCount[currentChar] += 1
            largestCount = 0
            # check the highest count letter
            for letter, count in charCount.items():
                largestCount = max(largestCount, count)
            currentWindowSize = (rightPointer + 1) - leftPointer
            # is the window minus the highest count letter less than or equal to k
            if currentWindowSize - largestCount <= k:
                # if it is, save the lenght of window to the max
                maxSubSLength = max(maxSubSLength, currentWindowSize)
                # increase the right pointer by 1
                rightPointer += 1
            # if its not
            else:
                # get the char at left pointer
                leftPointerChar = s[leftPointer]
                # remove it from the charCount
                charCount[leftPointerChar] -= 1
                charCount[currentChar] -= 1
                # increase the left Pointer by 1
                leftPointer += 1

        return maxSubSLength



