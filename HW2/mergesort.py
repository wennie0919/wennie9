array = [2,-3,4,11,-6,5.3,7]
class Solution(object):
    def mergesort(self,array):
        if len(array) < 1:        ##若數列小於一，直接回傳
            return array
        else:        
            middle=len(array)//2   ###把數列從中間切成一半
            left_array=array[:middle]   
            right_array=array[middle:]    ###分成左右兩邊，中間用分號
            
            self.mergesort(left_array)
            self.mergesort(right_array)   
            
       
        a=0
        b=0
        c=0
        d=[]
        
        if left_array:     
                d+=left_array
        else:
                d+=right_array
                
                
        while a <len(left) and b<len(right):
            if left[a] < right[b]:
                d.append(left_array.pop(0))    
                i+=1         ##就是java中的i++                   
               
            else:
                d.append(right_array.pop(0))
                j+=1
            
        while a < len(left) or q < len(right):   ###並列把兩個式子連起，再用if else做條件判斷
            if a < len(left):
                array[c] = left[a]
                a+=1
                c+=1
            else:
                array[c] = right[b]
                b+=1
                c+=1                               ###用兩個while迴圈做排大小
               
        return array
