## Breadth First Search :
廣度優先搜尋是一種圖形(graph)搜索演算法。以途中某一點(vertex, node)為起點開始走，走與他相鄰的點，對走過的點繼續進行先廣後深的搜尋。以樹(tree)來說即把同一層(level)的點走完，再繼續向下一層搜尋，直到找到目標點或遍尋全部點為止。廣度優先搜尋法屬於盲目搜索(uninformed search)是利用佇列(Queue)來處理，通常以迴圈的方式呈現。

## Depth First Search :
深度優先搜尋是從起點開始，任意選擇與起點相鄰的點走，走過的點會被標記下來，再將下一個點視為起點，繼續相同的走法，直到發現所有的點都已被標記過，即相鄰此點的所有點都已經走過了，則退回上一個分叉路口，繼續搜尋，直到所有的點都被標記過了，則搜索完畢。深度優先搜尋使用遞迴函式程式可以簡潔地進行書寫，並且狀態管理也很簡單，所以大多數情況還是用dfs來實現相關問題。

## 流程圖 ：
![](/images/bfs.jpg)
![](/images/dfs.jpg)
## BFS與DFS比較 ：
DFS與BFS大同小異，只是queue換成了stack而已。
舉一個例子來看:

![](/images/example.jpg)

#### BFS : 
要先看完一層目錄後，才會再看下一層。意思就是點進「image」後，要先看完「image」檔中下一層的所有檔，也就是會看到「apple」、「pig」兩個檔案。再繼續往下看，點進「apple」檔裡，會看到「red.jpg」、「small.jpg」。接者返回上一頁，點進「pig」檔裡，會看到「fat.jpg」、「cute.jpg」。

#### DFS :
看到「image」檔就會直接點入，首先會看到「apple」檔，再點進去會看到「red.jpg」、「small.jpg」。再返回「image」檔，才會看到有「pig」檔，點進去會看到「fat.jpg」、「cute.jpg」。

#### 結論：
若要在圖形中找出欲到達目標的最少步驟或尋找其中一個連通分支中的所有節點（擴散性），則可採用BFS。若要找出圖形的完整形狀或來儲存未訪問的節點，就可以採用DFS。







## 參考資料：
https://kopu.chat/2017/09/22/%E5%AF%A6%E4%BD%9Cgraph%E8%88%87dfs%E3%80%81bfs%E8%B5%B0%E8%A8%AA/
https://magiclen.org/dfs-bfs/
https://www.itread01.com/content/1541297601.html
https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/102866/
