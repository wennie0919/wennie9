## INSERT(新增資料):

顧名思義就是在BST中新增node(新增資料)，新增node需要先在BST中進行traversal，而且traversal的時間複雜度與height(樹高)成正比。
函式InsertBST()的概念，可以視為Search()的延伸，要從tree中先找到即將新增的node需要擺放的位置，「適當的位置」就會變成「新增的node」的「parent node」，「新增的node」就會變成其「left child」or「right child」。

## SEARCH(搜尋資料)：

就是要在tree中找尋一個資料，這是採用BST的Search()進行操作，主要特徵是：Key(Left) < Key(Current) < Key(Right)，判斷Current應該往left subtree走，還是往right subtree走。以下分為成功（Ａ）與失敗（Ｂ）做說明。

### Ａ、成功
先設置尋找的目標，再開始從tree頂端做比較，比頂端key(A)大往右走，比頂端key(A)小往左走，直至成功找到目標值為止，表示搜尋成功。
### Ｂ、失敗
先設置尋找的目標，再開始從tree頂端做比較，比頂端key(A)大往右走，比頂端key(A)小往左走，找不到了就回傳NULL，表示搜尋失敗。

## DELETE(刪除資料):

刪除資料根據刪除的「child個數」可以分為三種（如圖所示）：
1、刪除0個child: 因為欲刪除的資料下面沒有child，直接把資料的parent的left child或 right child導向NULL就好。
2、刪除1個child: 欲刪除的值下面有一個left child或right child，刪除之前，欲先把下面的child接到欲刪除（parent）的位子上，因此，要讓child取代parent就是把下面的child接到parent上就可以。
3、刪除2個child: 就要找下左邊最大或右邊最小的值先暫時移出一個，這樣就變成上述2的做法（刪除1個child），就把真正會被釋放記憶體的node的child指向新的parent及新的parent指向note，若真正被釋放的記憶體是剛剛暫時移出的值，就把它放回來。

## MODIFY(修改資料):
修改tree中的資料，不管是刪除還是新增，都屬於modify(修改資料)這一環節，將一個新的數字取代原先舊的數字，也將其舊的數字刪除，可以說是insert與delete的綜合，但須符合左邊是小於或等於目標，右邊是大於目標。


## 參考資料：
http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html
http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html
