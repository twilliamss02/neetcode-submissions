class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n

        for x in range(1, n):
            prefix[x] = prefix[x -1] * nums[x-1]
        
        for x in range(n-2, -1,-1):
            suffix[x] = suffix[x+1] * nums [x+1]

        for x in range(n):
            result[x] = prefix[x] * suffix[x]
        return result
        # Not solved by me. Looked up "suffix and prefix technique".