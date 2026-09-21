class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for s in strs:
            if tuple(sorted(s)) in myDict.keys():
                value = myDict[tuple(sorted(s))]
                value.append(s)
            else:
                myDict[tuple(sorted(s))] = [s]

        return list(myDict.values())

