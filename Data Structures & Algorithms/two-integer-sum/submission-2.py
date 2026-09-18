class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for l,r in enumerate(nums):
            diff = target - r
            if diff in my_dict:
                return [my_dict[diff], l]
            else:
                my_dict[r] = l