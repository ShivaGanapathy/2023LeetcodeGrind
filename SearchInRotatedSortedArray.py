class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ### Solution 1: O(logn) time O(1) space
        
        lp = 0 
        rp = len(nums) - 1
        
        while lp <= rp:
            
            mid = (lp + rp)//2
            
            if target == nums[mid]:
                return mid
            
            
            ### If we are in the left sorted portion
            if nums[mid] >= nums[lp]:
                if target > nums[mid]:
                    lp = mid + 1
                elif target < nums[lp]:
                    lp = mid + 1
                else:
                    rp = mid - 1
            ### If we are in the right sorted portion
            else:
                if target > nums[rp]:
                    rp = mid - 1
                elif target < nums[mid]:
                    rp = mid - 1
                else:
                    lp = mid + 1
            
                
        
        return -1
                
