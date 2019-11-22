## BST原理：
二元搜索樹(Binary Search Tree)是基於二元樹的一種，以利用在搜索、排序和提供資料集合基本結構，任何Currnet Node的Key若與其left child、right child之Key有以下關係(若pointer指向NULL則忽略)：Key(L)<Key(Current)<Key(R)，則可稱這棵樹為Binary Search Tree(BST)。


## INSERT(新增資料):

顧名思義就是在BST中新增node(新增資料)，新增node需要先在BST中進行traversal，而且traversal的時間複雜度與height(樹高)成正比。
函式InsertBST()的概念，可以視為Search()的延伸，要從tree中先找到即將新增的node需要擺放的位置，「適當的位置」就會變成「新增的node」的「parent node」，「新增的node」就會變成其「left child」or「right child」。

流程圖：
![](/images/insert.jpg)

## SEARCH(搜尋資料)：

這是採用BST的Search()進行操作，主要特徵是：Key(Left) < Key(Current) < Key(Right)，判斷Current應該往left subtree走，還是往right subtree走。以下分為成功（Ａ）與失敗（Ｂ）做說明。

### Ａ、成功
先設置尋找的目標，再開始從tree頂端做比較，比頂端key(A)大往右走，比頂端key(A)小往左走，直至成功找到目標值為止，表示搜尋成功。

流程圖：
![](/images/searchgood.jpg)


### Ｂ、失敗
先設置尋找的目標，再開始從tree頂端做比較，比頂端key(A)大往右走，比頂端key(A)小往左走，找不到了就回傳NULL，表示搜尋失敗。

流程圖：
![](/images/searchbad.jpg)

## DELETE(刪除資料):
刪除資料根據刪除的「child個數」可以分為三種（如圖所示）：
1、刪除0個child:因為「Ｉ」下面沒有child，直接把「Ｉ」的parent「Ｅ」的left child導向NULL。
2、刪除1個child:「Ｄ」下面有一個left child，刪除「Ｄ」之前，欲先使「Ｇ」接到「Ｄ」的位子上，「Ｄ」本身為「Ｂ」的right child，因此，要讓「Ｇ」取代「Ｄ」就是把「Ｇ」接到「Ｂ」的right child就可以。
3、刪除2個child:「Ｅ」有兩個child，不能直接刪除。就要找「Ｅ」下左邊最大或右邊最小的值先暫時移出一個，這樣就變成上述2的做法（刪除1個child），就把真正會被釋放記憶體的node的child指向新的parent及新的parent指向note，若真正被釋放的記憶體是剛剛暫時移出的值，就把它放回來。

流程圖：
![](/images/delete.jpg)

## MODIFY(修改資料):
依照需要修改的數值做刪除或新增的調整，可以說是insert與delete的綜合，修改過程中人須符合tree的原理，若不符合再做修改。
流程圖：
![](/images/modify.jpg)



## 結論：
新增資料(insert)、刪除資料(delete)本身都必須先執行一次搜尋(search)，而搜尋(search)的時間複雜度取決於BST的height(樹高)，insert、search、delete時間複雜度皆為O(height)。


參考資料：
http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html

http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html



 
