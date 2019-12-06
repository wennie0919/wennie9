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
        y = x % self.capacity
        
        if self.data[y] == None:
            self.data[y] = ListNode(x)
            
        else:
            new_node = ListNode(number)
            new_node.next = self.data[y]
            self.data[y] = new_node
        
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
    
    ## 參考資料： https://github.com/tonyforreal/Tony-learning-note/blob/master/HW4/hash_table_06170133.py 
    #http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
           # https://toyo0103.blogspot.com/2018/04/hash-table.html
               # https://www.nosuchfield.com/2016/07/29/the-python-implementationp-of-HashTable/
    
