class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {i : [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        # Set to keep track of all previously seen nodes
        visited = set()
        # Set to keep track of all nodes in current dfs path
        cycle = set()
        
        
        res = []
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            visited.add(course)
            
            
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            res.append(course)
            
            return True
            
            
            
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return res
            
            
                
        
