class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # two pointers of left and right
        leftPointer = 0
        rightPointer = len(nums) - 1
        # until right pointer reaches left pointer
        while leftPointer <= rightPointer:
            leftValue = nums[leftPointer]
            rightValue = nums[rightPointer]
            middlePointer = (leftPointer + rightPointer) // 2
            middleValue = nums[middlePointer]

            if middleValue == target:
                return middlePointer
            if rightValue == target:
                return rightPointer
            # if the middle value is larger than the left pointer, we can assume that the left to middle is ascending
            if middleValue > leftValue:
                # if ascending left to middle, we check if the value is between left and middle
                if target >= leftValue and target <= middleValue:
                    rightPointer = middlePointer - 1
                else:
                    leftPointer = middlePointer + 1
            else:
                # if the middle value is not larger than left, than that means the middle to right is ascending
                # if ascending middle to right, we check if the value is between middle and right
                if target >= middleValue and target <= rightValue:
                    leftPointer = middlePointer + 1
                else: 
                    rightPointer = middlePointer - 1
        return -1
