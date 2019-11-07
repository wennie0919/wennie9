## ＨＯＭＥＷＯＲＫ（11/8)

# Merge Sort(合併排序法)
Merge Sort屬於Divide and Conquer演算法，把數列先分成一半，再將分好的數列切一半，直到每個數列都變成單一元素，再來進行合併將單一元素兩兩合併，並小的排左邊，大的排右邊，在持續將合併好的數列合併，直到所有數列變成一個大數列。
時間複雜度皆為:O(n logn) 
每回合的合併需要花：O(n) 
總共需要回合數：O(log n)


# 學習歷程與問題
1.經過第一次的作業後，我其實蠻打擊的，我是一個看得懂code但打不出來的人，我這次主要是複習老師上課有講得一點code的內容，再打出來。
剛開始錯誤率一大堆，就不斷查資料錯在哪裡，最後終於擠出一點東西了！！
2.首先要先分割數列，將數列持續分半，直到它變成單一的數列。這個我花的時間相對比較少，只要把數列分成左右中三部分，排下去。
3.重點複雜的地方來了，要把它兩兩合併在排大小，我的邏輯沒有很好，所以想了很久時間才有一點想法，我剛開始用if左邊>右邊elif左邊<=右邊，但其他的我就寫不下去了。
就參考了以下網站找到解答，知道還要用while迴圈解題。
##  https://www.geeksforgeeks.org/merge-sort/
##  https://newaurora.pixnet.net/blog/post/224658923-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95---%E4%BD%BF%E7%94%A8python
##  https://medium.com/@amirziai/merge-sort-walkthrough-with-code-in-python-e4f76d90a4ea


# 程式架構設計說明

![](/images/merge.png)

# 流程圖

![](/images/S__89858114.jpg)
