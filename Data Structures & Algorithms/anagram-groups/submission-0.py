class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedDict = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in sortedDict:
                sortedDict[sortedWord] = []
            sortedDict[sortedWord].append(word)

        return list(sortedDict.values())