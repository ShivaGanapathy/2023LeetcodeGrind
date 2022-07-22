class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """Solution 1: O(n) time, O(1) space (Excluding return result)"""
        prefix_accumulator = 1
        final_array = [1 for _ in nums]
        
        for i in range(len(nums)):
            final_array[i] *= prefix_accumulator
            prefix_accumulator *= nums[i]
            
            
        postfix_accumulator = 1
        
        for i in range(len(nums)-1,-1,-1):
            final_array[i] *= postfix_accumulator
            postfix_accumulator *= nums[i]
            
        return final_array
            
        
