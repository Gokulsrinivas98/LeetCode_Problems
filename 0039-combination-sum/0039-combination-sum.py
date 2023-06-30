class Solution:
    def combinationSum(self, candidate: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(candidate,path,target,res):
            if target == 0:
                res.append(path)
                return
            for i in range(len(candidate)):
                if candidate[i] > target:
                    continue
                print(candidate[i],path,target-candidate[i],res)
                dfs(candidate[i:],path+[candidate[i]],target-candidate[i],res)
                
        dfs(candidate,[],target,res)
        return res