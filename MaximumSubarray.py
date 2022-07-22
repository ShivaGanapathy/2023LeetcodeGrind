class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        """Solution 1: O(n^2) time, O(1) space"""
        max_sum = min(nums)
        
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i,len(nums)):
                current_sum += nums[j]
                max_sum = max(current_sum, max_sum)
            
        return max_sum

        
        """Solution 2: O(n) time, O(1) space"""
        current_sum = -float('inf')
        max_sum = current_sum
        for i in range(len(nums)):
            if current_sum < 0:
                current_sum = nums[i]
            else:  
                current_sum += nums[i]
            
            max_sum = max(current_sum, max_sum)
            
        return max_sum
