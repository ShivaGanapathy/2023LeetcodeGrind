class ListNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.val = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.head = None
        self.tail = None
        self.capacity = k
        

    def insertFront(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        
        if not self.head and not self.tail:
            self.head = ListNode()
            self.tail = self.head
            self.head.val = value   
        else:
            new = ListNode()
            new.val = value
            new.next = self.head
            self.head.prev = new
            self.head = new
            
        self.size += 1
        
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        
        if not self.head and not self.tail:
            self.head = ListNode()
            self.tail = self.head
            self.head.val = value
        else:
            new = ListNode()
            new.val = value
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
            
        self.size += 1
            
        return True
        

    def deleteFront(self) -> bool:
        if not self.head:
            return False
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            
        else:
            self.head = self.head.next
            self.head.prev = None
            
        self.size -= 1
        
        return True
        
        

    def deleteLast(self) -> bool:
        
        if not self.head:
            return False
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            
        self.size -= 1
        
        return True
        

    def getFront(self) -> int:
        if not self.head:
            return -1
        return self.head.val
        

    def getRear(self) -> int:
        if not self.tail:
            return -1
        return self.tail.val
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
