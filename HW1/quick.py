def quicksort(a):
    if len(a)<2:         
        return a
    else:
        pivot=a[0]      #數列的第一個數字作為基準點pivot
        less=[i for i in a[1:] if i<pivot]
                            #小於pivot的放置less數列之中，a[1:]是把a從1（第二個位置的數字）開始往後找，因為0為pivot
        more=[i for i in a[1:]if i>=pivot]
                           #大於及等於的放置more數列中
        return quicksort(less)+[pivot]+quicksort(more)
                           #將新的數列重新整理，quicksort(less)和quicksort(more)丟回if len(a)<2:，若有兩個以上的數字，再重新分類
                           #直到所有list中都只剩下一個數，分不出『新的數列』為止，便會停止分類
                          
list=[4,8,3,0,11,8,16,1,6,9]
quicksort(list)
 
 Out [0, 1, 3, 4, 6, 8, 8, 9, 11, 16]
