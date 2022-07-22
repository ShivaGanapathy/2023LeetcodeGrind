class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """Solution 1: O(n^2) time, O(1) space"""
        max_sum = max(nums)
        for i in range(len(nums)):
            current_product = nums[i]
            for j in range(i+1, len(nums)):
                current_product *= nums[j]
                max_sum = max(current_product, max_sum)
                
                
        return max_sum
    
    
    
        """Solution 2: O(n) time, O(1) space"""
        current_min, current_max = 1,1
        max_product = max(nums)
        for num in nums:    
            if num == 0:
                current_min, current_max = 1,1
            
            temp = num * current_max
            current_max = max(num * current_max, num*current_min, num)
            current_min = min(temp, num*current_min, num)
            max_product = max(current_max, max_product)
            
            
        return max_product
