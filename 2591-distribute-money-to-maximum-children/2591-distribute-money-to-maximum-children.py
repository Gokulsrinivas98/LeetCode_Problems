class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children: return -1
        elif money == children: return 0
        count,rem = money//8,money%8 
        while count >=0:
            if count + rem >= children:
                if children == count+1 and rem == 4 or children == count and rem!=0: 
                    return count-1
                elif count>children:
                    count-=1
                    rem+=8
                else:
                    return count
            else:
                count-=1
                rem+=8
        return -1            