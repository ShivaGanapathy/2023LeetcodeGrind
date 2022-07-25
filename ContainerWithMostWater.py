class Solution:
    def maxArea(self, height: List[int]) -> int:
        ### O(n) time solution O(1) space
        lp = 0
        rp = len(height) - 1
        max_area = 0
        
        while lp < rp:
            width = rp - lp
            current_height = min(height[lp], height[rp])
            
            area = width * current_height
            
            max_area = max(area, max_area)
            
            if height[lp] <= height[rp]:
                lp += 1
                
            else:
                rp -= 1
                
            
            
        return max_area
            
            
