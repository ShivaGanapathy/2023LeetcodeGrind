class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        """Solution 1: O(n) time, O(n) space"""
        number_set = set()
        for num in nums:
            if num in number_set:
                return True
            number_set.add(num)
            
        return False
    
    
    
        """Solution 2: O(n log n) time, O(1) space"""
        nums.sort()
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
            
        return False
