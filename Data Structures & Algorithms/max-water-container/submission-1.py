class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        area = 0

        while l < r:
            short_bar = min(heights[l], heights[r])
            temp = (short_bar) * (r - l) 
            area = max(area, temp)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
            
                
        return area
