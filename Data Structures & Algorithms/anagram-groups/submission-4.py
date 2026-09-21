class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for s in strs:
            if str(sorted(s)) in myDict.keys():
                value = myDict[str(sorted(s))]
                value.append(s)
            else:
                myDict[str(sorted(s))] = [s]

        return list(myDict.values())

