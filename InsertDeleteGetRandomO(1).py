class RandomizedSet:

    def __init__(self):
        self.element_to_index = {}
        self.elements = []

    def insert(self, val: int) -> bool:
        if val not in self.element_to_index:
            self.element_to_index[val] = len(self.elements)
            self.elements.append(val)
            return True
        
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.element_to_index:
            # Before removing this entry from the hashmap and list, we need to swap the entry to the last position in the list
            
            temp = self.elements[-1]
            self.elements[-1] = val
            self.elements[self.element_to_index[val]] = temp
            self.element_to_index[temp] = self.element_to_index[val]
            self.elements.pop()
            del self.element_to_index[val]
            return True
        
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.elements)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
