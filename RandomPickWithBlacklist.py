class Solution:

    def __init__(self, n: int, blacklist: List[int]):    
        # Create a hashset that will keep track of all white listed numbers in the upper half
        upper_half_whitelist = set([i for i in range(n - len(blacklist), n)])
        
        for num in blacklist:
            if num in upper_half_whitelist:
                upper_half_whitelist.remove(num)
        
        # Now map all bottom half blacklisted numbers to top half whitelisted numbers
        white_nums = iter(upper_half_whitelist)
        
        black_mapping = {}
        
        # Iterate through all bottom half blacklisted nums
        
        for num in blacklist:
            if num < n - len(blacklist):
                black_mapping[num] = next(white_nums)
                
        
        self.n = n
        self.black_mapping = black_mapping
        self.blacklist = blacklist
                
    def pick(self) -> int:
        x = random.randint(0, self.n - len(self.blacklist) - 1)
        
        if x in self.black_mapping:
            return self.black_mapping[x]
        else:
            return x
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
