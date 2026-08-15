class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {
        // first remove all non alphanumeric letters
        const strippedString = s.toLowerCase().replace(/[^a-z0-9]/g, "")
        if (strippedString.length === 1) return true;
        // setup a front pointer and back pointer
        let frontPointer = 0;
        let backPointer = strippedString.length - 1;
        // find the middle point
        const middleIndex = Math.round((strippedString.length - 1) / 2);
        // setup a while loop, while first pointer is not at middle point, continue
        while (frontPointer !== middleIndex) {
            const frontPointerValue = strippedString[frontPointer];
            const backPointerValue = strippedString[backPointer];
            if (frontPointerValue !== backPointerValue) {
                return false;
            }
    
            //move both indexes forward
            frontPointer += 1
            backPointer -= 1
        }
        return true;
    }
}
