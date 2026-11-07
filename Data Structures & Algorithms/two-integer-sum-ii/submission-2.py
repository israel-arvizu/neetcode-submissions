class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       # have a pointer for base number
       basePointer = 0
       # have a pointer for moving number
       movingPointer = 1
       # keep track of base pointers to avoid looping through the same
       clearedPointerValues = set()
       
       # while base pointer is not at last number
       while basePointer < len(numbers) - 1:
        basePointerValue = numbers[basePointer]
        if basePointerValue in clearedPointerValues:
            basePointer += 1
            continue
        else:
            clearedPointerValues.add(basePointerValue) 
        movingPointer = basePointer + 1
        while movingPointer < len(numbers):
            movingPointerValue = numbers[movingPointer]
            tempPointerSum = basePointerValue + movingPointerValue
            if tempPointerSum == target:
                return [basePointer + 1, movingPointer + 1]
            if tempPointerSum > target:
                break
            else:
                movingPointer += 1
        basePointer += 1
       return [1, 2]
        
        