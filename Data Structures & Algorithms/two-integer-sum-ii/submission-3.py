class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # one pointer on the low end
        lowEndPointer = 0
        # one pointer on the high end
        highEndPointer = len(numbers) - 1
        # while pointers dont intersect
        while lowEndPointer < highEndPointer:
            pointerValueSum = numbers[lowEndPointer] + numbers[highEndPointer]
            if pointerValueSum == target:
                return [lowEndPointer + 1, highEndPointer + 1]
            if pointerValueSum < target:
                lowEndPointer += 1
            if pointerValueSum > target:
                highEndPointer -= 1
        