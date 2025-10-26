class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        distinctValues = list(set(nums))
        memo = dict.fromkeys(distinctValues, 0)
        for n in nums:
            memo[n] += 1
        
        for key, value in memo.items():
            if value == 1:
                return key