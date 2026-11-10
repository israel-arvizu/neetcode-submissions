class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        minValue = nums[0]
        # pointers
        leftIndex = 0
        rightIndex = len(nums) - 1

        while leftIndex <= rightIndex:
            leftValue = nums[leftIndex]
            rightValue = nums[rightIndex]

            if leftValue < rightValue:
                minValue = min(leftValue, minValue)
                break
            
            middlePointer = (leftIndex + rightIndex) // 2 
            middleValue = nums[middlePointer]
            minValue = min(minValue, middleValue)

            if(leftValue > middleValue):
                rightIndex = middlePointer - 1
            else:
                leftIndex = middlePointer + 1

    
        return minValue

        