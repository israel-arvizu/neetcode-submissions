class Solution:
    def isValid(self, bracketString: str) -> bool:
        if len(bracketString) <= 1:
            return False

        openBrackets = {"(", "{", "["}
        closeBrackets = {")", "}", "]"}
        closeBracketTypeMap = {")": "(", "}": "{", "]": "["}
        bracketStack = []

        # go through the s, as we go through it,
        for item in bracketString:
            # add open brackets to the stack
            if item in openBrackets:
                bracketStack.append(item)
            # once we encounter a close bracket
            if item in closeBrackets:
                if not len(bracketStack):
                    return False
                poppedItem = bracketStack.pop()

                # we check if the open bracket is its opposite
                if poppedItem == closeBracketTypeMap[item]:
                    # if it is
                    continue
                else:
                    # if its not, return false
                    return False
        # once we finish going through s, return true if nothing remains in the stack
        if len(bracketStack) > 0:
            return False
        else: 
            return True
