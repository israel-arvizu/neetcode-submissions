class Solution:
    def isValid(self, bracketString: str) -> bool:
        if len(bracketString) <= 1:
            return False

        closeBracketTypeMap = {")": "(", "}": "{", "]": "["}
        bracketStack = []

        # go through the s, as we go through it,
        for item in bracketString:
            # add open brackets to the stack
            if item in closeBracketTypeMap:
                if bracketStack and bracketStack[-1] == closeBracketTypeMap[item]:
                    poppedItem = bracketStack.pop()
                else:
                    # if its not, return false
                    return False
            else:
                bracketStack.append(item)

        # once we finish going through s, return true if nothing remains in the stack
        return True if not bracketStack else False
