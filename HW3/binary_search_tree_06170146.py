class TreeNode(object):
    def __init__(self, data):
        self.left = None        
        self.data = data      
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data            
    def delete(root, target): 
        if root is None: 
            return root  
        if target < root.target: 
            root.left = delete(root.left, target)   
        elif(target > root.target): 
            root.right = delete(root.right, target)   
        else:
            if root.left is None : 
                temp = root.right  
                root = None 
                return temp            
            elif root.right is None : 
                temp = root.left  
                root = None
                return temp  
        temp = minValueNode(root.right)   
        root.target = temp.target  
        root.right = delete(root.right , temp.target) 
        return root  
    def search(self, root, target):
        if root.val==target:
            return root
        elif target<root.val:
            return Solution().search(root.left,target)
        elif target>root.val:
            return Solution().search(root.right,target)
        else:
            return None
        
    def modify(self, root, val, new_val):
        if root:
            if root.val == val:
                root.val = new_val       
        if root.left:
            self.modify(root.left, val, new_val)       
        if root.right:
            self.modify(root.right, val, new_val)           
        return root
    def PrintTree(self):
        print(self.data)

root = Node(1)
root.PrintTree()



##參考資料：https://medium.com/@stephenagrice/how-to-implement-a-binary-search-tree-in-python-e1cdba29c533
####https://www.geeksforgeeks.org/modify-binary-tree-get-preorder-traversal-using-right-pointers/
###https://codereview.stackexchange.com/questions/229921/binary-tree-sort-algorithm-python
