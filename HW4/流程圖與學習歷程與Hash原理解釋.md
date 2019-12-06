### HASH TABLE（雜湊表）：

要先將資料先透過雜湊函式取得數字，再去除以要分出的 table 的大小，其餘數就是 index，再依照 index 值將數值分類入 buckets 中。
要達到這個目標，必須引入 Hash Function，將 Key 對應到符合 table 大小的範圍內， index = h (Key) ，即可成為 Hash Table 的 index。
Hash Table 的核心概念就是要解決"避免記憶體空間浪費"的缺點。

### HASH FUNTION(雜湊函式):

一種輸入的字串，然後輸出數字的函數。也就是「將字串對應至數字」。把數據壓縮成雜湊值，保護數據且固定不易發生碰撞。例：“dog” → 雜湊函數 → 3。
我們需要將MD5加密，十六進位轉為十進位的純數字。

### 雜湊表的效能

平均情況：搜尋、插入、刪除，皆為 O(1)

最壞情況：搜尋、插入、刪除，皆為 O(n)

O(1) 稱為常數時間(Constant Time)，代表不論雜湊表多麼大，耗費的時間皆維持不變的意思。

### COLLISION(碰撞)：
發生同一個 index 對應到相同的儲存槽的情況，這將會使得查詢數據失敗。如果發生碰撞，則用linked list將兩者連結，資料就不會被取代掉。

![](/images/collision.jpg)


### 流程圖：



### 學習歷程：



#### 參考資料：
https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/
https://carlos-studio.com/2018/01/21/%E6%BC%94%E7%AE%97%E6%B3%95-%E9%9B%9C%E6%B9%8A%E8%A1%A8hash-table/
http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
