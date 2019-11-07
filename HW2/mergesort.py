array = [2,-3,4,11,-6,5.3,7]
class Solution(object):
    def mergesort(self,array):
        if len(array) < 1:        
            return array
        else:        
            middle=len(array)//2
            left_array=array[:middle]
            right_array=array[middle:]
            
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
                i+=1
               
            else:
                d.append(right_array.pop(0))
                j+=1
            
        while a < len(left) or q < len(right):
            if a < len(left):
                array[c] = left[a]
                a+=1
                c+=1
            else:
                array[c] = right[b]
                b+=1
                c+=1 
                
            

        return array
