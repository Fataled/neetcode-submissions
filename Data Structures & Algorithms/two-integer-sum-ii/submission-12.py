class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = None
        for l in range(len(numbers)):
            if seen != None and numbers[l] == seen:
                continue
            for r in range(len(numbers) - 1, -1, -1):
                if numbers[l] + numbers[r] == target:
                    return [l + 1, r + 1]
                seen = numbers[l]
