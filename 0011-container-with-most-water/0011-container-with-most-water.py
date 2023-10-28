class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        max_area = 0
        max_height = max(height)
        while start < end and max_height*(end-start) > max_area:
            # area = len*bred = abs(min(height[start],height[end]) * (start - end))
            max_area = max(max_area,min(height[start],height[end]) * (end - start))
            
            
            if height[start] <= height [end]:
                start +=1
            else:
                end -= 1
        return max_area