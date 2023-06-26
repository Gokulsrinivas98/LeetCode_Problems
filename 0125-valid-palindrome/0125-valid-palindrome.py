class Solution:
    def isPalindrome(self, s: str) -> bool:
        list=[]
        for i in s:
            if i.isalnum():
                list.append(i)
        stri = ""
        string = stri.join(list).lower()
        revstring = string[::-1]
        return string == revstring