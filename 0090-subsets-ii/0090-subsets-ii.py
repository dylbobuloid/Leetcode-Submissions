class Solution(object):
    def subsetsWithDup(self, nums):

        res = []
        nums.sort()

        def dfs(i, cur):
            if i == len(nums):
                res.append(cur[:])
                return
            if i > len(nums):
                return
            
            cur.append(nums[i])
            dfs(i+1, cur)
            cur.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, cur)
        dfs(0,[])
        return res
        