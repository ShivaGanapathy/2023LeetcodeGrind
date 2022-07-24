class Solution:
    def findMin(self, nums: List[int]) -> int:
      
        ### Solution 1: O(logn) time O(1) space
        lp = 0 
        rp = len(nums) - 1
        
        while lp < rp:
            mid = (lp + rp)//2
            
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            
            # If we are on the left sorted portion and the smaller number is on the right sorted side
            if (nums[lp] <= nums[mid] and nums[mid] > nums[rp]):
                lp = mid + 1
            else:
                rp = mid - 1
            
                
        return nums[lp]
