class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = list()

        for l in range(len(nums)):
            for r in range(len(nums) -1, l, -1):
                if nums[l] + nums[r] == target:
                    values.append(l)
                    values.append(r)
                    break
        return values