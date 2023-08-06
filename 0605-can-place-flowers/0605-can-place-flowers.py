class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                # Check if the previous and next plot are also empty or out of bounds
                prev_empty = (i == 0 or flowerbed[i - 1] == 0)
                next_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                if prev_empty and next_empty:
                    flowerbed[i] = 1  # Plant a flower
                    count += 1
                    i += 1  # Move to the next empty plot (skip one plot as we can't plant adjacent flowers)
            i += 1
        
        return count >= n
        