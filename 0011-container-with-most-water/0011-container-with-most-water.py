class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        max_area = 0
        while start < end:
            # area = len*bred = abs(min(height[start],height[end]) * (start - end))
            area = abs(min(height[start],height[end]) * (start - end))
            max_area = max(area,max_area)
            print(max_area,start,end)
            if height[start] < height [end]:
                start +=1
            else:
                end -= 1
        return max_area