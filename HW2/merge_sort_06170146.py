class Solution(object):
    def merge_sort(self, nums):
        
        if len(nums)>1:     ##若數列大於一，即可執行下面程式
            middle=len(nums)//2  ###把數列從中間切成一半
            left=nums[:middle]
            right=nums[middle:]    ###分成左右兩邊，中間用分號
            
            self.merge_sort(left) 
            self.merge_sort(right) 
            
            a=0
            b=0
            c=0
                
            while b<len(left) and c<len(right):    ###並列把兩個式子連起，再用if else做條件判斷，and是“且”的意思
                if  left[b]<right[c]:   ##左邊小於右邊，則數列顯示左邊在前面
                    nums[a]= left[b]
                    b+=1         ##就是java中的i++，意思是前一個已經比大小完了，要向後一個推進，進行下一組的比大小     
                    a+=1
                else:
                    nums[a]= right[c]   ##同理，右邊小於左邊，則數列顯示右邊在前面
                    c+=1
                    a+=1    
                    
            while b<len(left) or c<len(right):     ###並列把兩個式子連起，再用if else做條件判斷，這裡用or區分，與上面的and不同，or是“或”
                if  b<len(left):
                    nums[a]= left[b]
                    b+=1
                    a+=1
                else:
                    nums[a]= right[c]
                    c+=1
                    a+=1                    ###用兩個while迴圈做排大小
                    
                    
list=[3,55,12,-2,75,9,16]
Solution().merge_sort(list)   ##顯示mergesort的比較結果
print(list)             ##印出數列
