class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */

    twoSum(nums: number[], target: number): number[] {
        let stablePointer = 0
        let movingPointer = 1
        const maxLength = nums.length

        while(stablePointer !== movingPointer){
            const stableValue = nums[stablePointer];
            const movingValue = nums[movingPointer];

            if(stableValue + movingValue === target) 
                return [stablePointer, movingPointer]
  
            const newMovingPointer = movingPointer++
            //if max length is lesser than the newMovingPointer
            //ex: 3, 3, will fail because nums[3] wont exist
            if(maxLength <= newMovingPointer){
                // reset moving pointer and move up stablePointer

                //if the new stable pointer reaches maxLenght - 1, break early
                //ex: 3, 2. becuase nums[2] will return the last value
                stablePointer = stablePointer + 1;
                if(maxLength - 1  <= stablePointer){
                    break;
                }
                movingPointer = stablePointer + 1;
            } 
        }
        return [stablePointer, movingPointer]
    }
}
