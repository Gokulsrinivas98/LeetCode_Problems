class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row, col = len(img), len(img[0])
        res = [[0]*col for i in range(row)]
        dirs = [[0,0],[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        for i in range(row):
            for j in range(col):
                temp = [img[i+m][j+n] for m,n in dirs if 0<=i+m<row and 0<=j+n<col]
                res[i][j] = sum(temp)//len(temp)
        return res