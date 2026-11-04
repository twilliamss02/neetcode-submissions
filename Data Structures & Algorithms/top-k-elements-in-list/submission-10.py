class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_dict = Counter(nums)
        return sorted(sorted_dict, reverse=True, key=lambda x: sorted_dict[x])[:k]