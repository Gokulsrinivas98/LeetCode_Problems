class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        #We are setting up a restore point
        restore = set()
        #Defining a function to perform backtracking recursively
        def recursive_backtracking(i,sequence):
            #Check if the number of elements in the sequence is more then 1 add it to restoree
            if len(sequence)>1:
                restore.add(tuple(sequence)) 
            #Check if the function reaches the end of the list, then exit out of recursion
            if i == len(nums):
                return
            # Check to make sure the subsequence is non-decreasing if we want to pick the current element.
            if not sequence or nums[i]>= sequence[-1]:
                recursive_backtracking(i+1,sequence+[nums[i]])
            #Checking next element    
            recursive_backtracking(i+1,sequence)
        #Start recursion
        recursive_backtracking(0,[])
        return restore