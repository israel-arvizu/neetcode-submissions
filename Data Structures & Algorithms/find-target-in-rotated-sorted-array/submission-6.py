class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftPointer, rightPointer = 0, len(nums) - 1

        # until right pointer reaches left pointer
        while leftPointer <= rightPointer:
            leftValue, rightValue = nums[leftPointer], nums[rightPointer]
            middlePointer = (leftPointer + rightPointer) // 2
            middleValue = nums[middlePointer]

            if middleValue == target:
                return middlePointer
            # left to middle is ascending
            if leftValue <= middleValue:
                if target < leftValue or target > middleValue:
                    leftPointer = middlePointer + 1
                else:
                    rightPointer = middlePointer - 1
            # middle to right is ascending
            else:
                if target > rightValue or target < middleValue:
                    rightPointer = middlePointer - 1
                else: 
                    leftPointer = middlePointer + 1
        return -1
