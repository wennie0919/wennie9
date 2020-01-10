## Hash Table
HASH TABLE（雜湊表）：
要先將資料先透過雜湊函式取得數字，再去除以要分出的 table 的大小，其餘數就是 index，再依照 index 值將數值分類入 buckets 中。 要達到這個目標，必須引入 Hash Function，將 Key 對應到符合 table 大小的範圍內， index = h (Key) ，即可成為 Hash Table 的 index。 Hash Table 的核心概念就是要解決"避免記憶體空間浪費"的缺點。

HASH FUNTION(雜湊函式):
一種輸入的字串，然後輸出數字的函數。也就是「將字串對應至數字」。把數據壓縮成雜湊值，保護數據且固定不易發生碰撞。例：“dog” → 雜湊函數 → 3。 我們需要將MD5加密，十六進位轉為十進位的純數字。
