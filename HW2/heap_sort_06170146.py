class Solution(object):   
    def heap_sort( self , nums ): ###heap_sort為一個平台，設置一個funtion
        
        a =len(nums)   ###a=數列的長度
        
        for i in range( a - 1, - 1, - 1):  #用for迴圈來執行位子
            Solution().heapify(nums,a,i)
            
        for i in range( a - 1, 0 , - 1):
            nums[i],nums[0]=nums[0],nums[i]
            Solution().heapify( nums, i, 0)  ###最大值與最後的值需要交換位子，所以用heapify來讓數列重新排列組合
            
        return nums
    

    def heapify( self, nums, a, i):   ###heapify為一個平台，設置一個funtion
        root = i   ##樹根
        L = 2 * i + 1  ###left=L
        R = 2 * i + 2  ###right=R 這裡是因為有左右兩邊的孩子，為了區分它們而設置
        
        if L < a and nums[ L ] > nums[ root ]:
            root = L   ##左邊若大於樹根，那左邊的孩子就會取代樹根的位子
        if R < a and nums[R] > nums[ root ] :
            root = R   ##右邊若大於樹根，那右邊的孩子就會取代樹根的位子
        if root != i:  ###可以更換位子
            nums[ root ],nums[ i ]=nums[ i ],nums[ root ]
            Solution().heapify( nums , a , root )
y = [66,1,4,22,78,5,9]
Solution().heap_sort(y)
