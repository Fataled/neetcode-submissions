class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = [[] for i in range(len(nums) + 1)]
        myDict ={}

        for n in nums:
            myDict[n] = 1 + myDict.get(n, 0)
        
        for key,v in myDict.items():
            l[v].append(key)

        res = []
        for i in range(len(l) -1, 0, -1):
            for num in l[i]:
                res.append(num)
                if len(res) == k:
                    return res



