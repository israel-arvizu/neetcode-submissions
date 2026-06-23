class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const valueIndexMap = new Map();
        let goldenIndexArray = [0, 1]

        for (let index = 0; index < nums.length; index++) {
            //check if the target - number exist in our hasmap
            const difference = target - nums[index];
            const valueIndeces = valueIndexMap.get(difference);
            //if it does
            if(typeof valueIndeces === 'number'){
              // check if the indeces are the same, if it is, skip, else return the goldenIndex
              if(valueIndeces !== index){
                goldenIndexArray = [valueIndeces, index];
                break;
              }
            }

            //if it does not, add the number to our map
            valueIndexMap.set(nums[index], index)
        }
        return goldenIndexArray
 
    }
}
