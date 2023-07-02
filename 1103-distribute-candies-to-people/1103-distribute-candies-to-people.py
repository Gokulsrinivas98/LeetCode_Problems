class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0]*num_people
        i,j = 0,1
        while candies > 0:
            if i==len(res):
                i=0
            if candies >= j:
                res[i]  += j
                candies -=j
                j+=1
            else: 
                res[i] += candies
                break
            i+=1
        return res