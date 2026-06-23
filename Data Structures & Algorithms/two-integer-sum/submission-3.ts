class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const valueIndexMap = new Map();

        for (let index = 0; index < nums.length; index++) {
            //check if the target - number exist in our hasmap
            const difference = target - nums[index];

              // check if the indeces are the same, if it is, skip, else return the goldenIndex
              if(valueIndexMap.has(difference)){
                return [valueIndexMap.get(difference)!, index]
              }
            
            //if it does not, add the number to our map
            valueIndexMap.set(nums[index], index)
        }
    }
}
