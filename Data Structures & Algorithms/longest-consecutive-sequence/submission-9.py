class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == [] or len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        nums = set(nums)
        longest_so_far = 1
        possible_longest = 1
        for index, number in enumerate(sorted(list(nums))):
            if (number + 1) in nums:
                possible_longest += 1
                
                continue



            if possible_longest >= longest_so_far:
                longest_so_far = possible_longest
                possible_longest = 1
           
            

        return longest_so_far
