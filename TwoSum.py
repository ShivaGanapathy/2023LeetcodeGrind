class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """Solution 1: O(n^2) time, O(1) space"""
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j
                           
        """Solution 2: O(nlogn) time, O(1) space"""
        arr = [(nums[i], i) for i in range(len(nums))]
        arr.sort()
        lp = 0
        rp = len(arr) - 1
        
        while lp < rp:
            if arr[lp][0] + arr[rp][0] > target:
                rp -= 1
            elif arr[lp][0] + arr[rp][0] < target:
                lp += 1
            else:
                return sorted([arr[lp][1],arr[rp][1]])
            
        """Solution 3: O(n) time, O(n) space"""
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return hashmap[complement], i
            hashmap[num] = i
            
        
            
        
                
        
        
        
        
