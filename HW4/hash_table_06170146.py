from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    
    def add(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x%self.capacity
        
        if self.contains(key) != True:
            if self.data[y] != None:
                new = ListNode(x)
                new.next = self.data[y]
                self.data[y] = new
            else:
                self.data[y] = ListNode(x)
        else:
            return
        
    def remove(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x%self.capacity
        z = self.data[y]
       
        if self.contains(key) != True:
            return 
        
        else:
            if z.val == x:
                self.data[y] = self.data[y].next
                return 

            else:
                point = self.data[y]
                while point.next.val != x:
                    point = point.next
                point.next = point.next.next
                
    def contains(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x % self.capacity
        z = self.data[y]
        
        while z:
            if z.val != x:
                z = z.next
            else:
                return True
        
        return False
