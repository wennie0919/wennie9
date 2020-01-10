def quick_sort(list): #排小值、大值、目標
    smaller = []
    bigger = []
    keylist = []

    if len(list) <= 1: #假如list長度小於等於1, 直接回傳結果
        return list

    else:
        key = list[0] #第一個是key數（目標對象）
        for i in list:
            if i < key: #i若比目標值小，繼續跑（排前面）
                smaller.append(i)
            elif i > key: #i若比目標值大，繼續跑（排後面）
                bigger.append(i)
            else:
                keylist.append(i)
    smaller = quick_sort(smaller)
    bigger = quick_sort(bigger)
    return smaller + keylist + bigger #顯示出（偏小、目標、偏大）
    
    
    list=[3,9,5,7,4,2,1]
    quick_sort(list)
    [1, 2, 3, 4, 5, 7, 9]
