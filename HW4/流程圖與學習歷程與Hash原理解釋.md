## HASH TABLE（雜湊表）：

要先將資料先透過雜湊函式取得數字，再去除以要分出的 table 的大小，其餘數就是 index，再依照 index 值將數值分類入 buckets 中。
要達到這個目標，必須引入 Hash Function，將 Key 對應到符合 table 大小的範圍內， index = h (Key) ，即可成為 Hash Table 的 index。
Hash Table 的核心概念就是要解決"避免記憶體空間浪費"的缺點。

## HASH FUNTION(雜湊函式):

一種輸入的字串，然後輸出數字的函數。也就是「將字串對應至數字」。把數據壓縮成雜湊值，保護數據且固定不易發生碰撞。例：“dog” → 雜湊函數 → 3。
我們需要將MD5加密，十六進位轉為十進位的純數字。

## 雜湊表的效能

平均情況：搜尋、插入、刪除，皆為 O(1)

最壞情況：搜尋、插入、刪除，皆為 O(n)

O(1) 稱為常數時間(Constant Time)，代表不論雜湊表多麼大，耗費的時間皆維持不變的意思。

## COLLISION(碰撞)：
發生同一個 index 對應到相同的儲存槽的情況，這將會使得查詢數據失敗。如果發生碰撞，則用linked list將兩者連結，資料就不會被取代掉。

![](/images/collision.jpg)


## 流程圖：

![](/images/t.jpg)

## 學習歷程：
剛開始的想法是老師教的用ＭＤ5來進行加密，把複雜的文字轉換成密碼，以便各國語言統一，每個國家自行決定編碼，這裡中文就是以“utf-8”表示，在複製老師所要求的格式，設兩個class，一個設ListNode，另一個設MyHashSet，由於我在HW3中忘記另一個class，被扣了很多分數，所以這次特別記得要有兩個。
![](/images/list.png)

#### add:
把在add裡面，剛開始要先設定好參數，x就為加密後要的int，y就表示x去除以capacity所設於下來的數(index)，我在用if...else，把欲加入的加進去，測資之後是true的！這讓我信心大增。
![](/images/add.png)
![](/images/test1.png)
#### remove:
剛開始的左法一樣是設x、y，不過還要加一個z設成self.data[y]，若有contain是true的話則回傳，要不然數值要被next所取代。這裡我的邏輯想了蠻久的，不知道next到底怎麼去設置使用。
![](/images/remove.png)

#### contain:
contain是最先完成的程式，不過因為順序的關係，我就最後講，以上的add跟remove都是以這個基礎出發。我就設int為x，由於還需要一個index餘數，我將餘數設成y，index餘數就是用x去除以capacity所設於下來的數，再設一個self.data[y]以z值替代，最後我在用了一個while迴圈把if...else包在裡面。
![](/images/contain.png)
![](/images/test1.png)

最後測資：
是成功的，中間試了一大堆，很雜亂，我就不貼上來了，以最後成功為最終結果。
![](/images/test.png)
#### 參考資料：
https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/
https://carlos-studio.com/2018/01/21/%E6%BC%94%E7%AE%97%E6%B3%95-%E9%9B%9C%E6%B9%8A%E8%A1%A8hash-table/
http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
