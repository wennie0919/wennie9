class Solution(object):
    
    def heap_sort(self,r):   #設一個funtion
        Ans = [] 
        self.heapify(r)
        
        
        while len(r) != 0: #用while迴圈跑list
            Ans.append(r.pop(0)) 
            self.heapify(r) 
            
            Ans.reverse()
        
        return Ans ##把剛剛的結果顯示出來
    
    def build_heap(self, r):
        a = len(r)  ###設長度是a
        last_node = a-1  ###這是最後的節點
        parent = (a-1-1)//2  
        

        for parent in range(parent,-1,-1):  #父母需往回跑，所以是負一
            self.heapify(r,a,parent) 
            
    def heapify(self,r,a,i):
        
        if i >= n:  # 若i大於n，直接回傳，大於n才可往下跑
            return nums

        root=i
        L=2*i+1  #left
        R=2*i+2  #right
        
        if left < a and r[L]>r[root]:
            root = L
            
        if right < a and r[R] > r[root] :
            root = R
            
        if root != i:  #可以更換位子
            r[root],r[i]=nums[i],r[root]
            Solution().heapify(r,a,root)
