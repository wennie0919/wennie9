## Breadth First Search :
廣度優先搜尋是一種圖形(graph)搜索演算法。以途中某一點(vertex, node)為起點開始走，走與他相鄰的點，對走過的點繼續進行先廣後深的搜尋。以樹(tree)來說即把同一層(level)的點走完，再繼續向下一層搜尋，直到找到目標點或遍尋全部點為止。廣度優先搜尋法屬於盲目搜索(uninformed search)是利用佇列(Queue)來處理，通常以迴圈的方式呈現。

## Depth First Search :
深度優先搜尋是從起點開始，任意選擇與起點相鄰的點走，走過的點會被標記下來，再將下一個點視為起點，繼續相同的走法，直到發現所有的點都已被標記過，即相鄰此點的所有點都已經走過了，則退回上一個分叉路口，繼續搜尋，直到所有的點都被標記過了，則搜索完畢。深度優先搜尋使用遞迴函式程式可以簡潔地進行書寫，並且狀態管理也很簡單，所以大多數情況還是用dfs來實現相關問題。

## 學習歷程 :
剛開始套用老師給的格式，其實覺得老師給我們格式幫我們省去了很多時間，我們不用天馬行孔去想格式要怎麼寫，設定init跟addedge，老師都有給，再來就是bfs了
![](/images/to.png)
因為我對於數字的邏輯，尤其是找數字會容易搞混，所以自己練習了幾次自己畫圖然後用bfs、dfs找出step1、step2的算法，就是罩上課的寫，經過練習比較熟悉之後再開始想程式碼的邏輯，bfs就是需要用while迴圈去做，先設置佇列(Queue)與答案的顯示，再用while迴圈來做定義一個pop的範圍。
![](/images/bsftu.png)
我覺得bfs、dfs其實差不多，只是dfs需要「走到底」，爾且把queue換成了stack，他們邏輯是差不多的，程式碼的pop與append都是大二有上過的內容，寫起來較順，不想前幾次作業，都會學新的程式碼。
![](/images/dfstu.png)
#### 測試結果：

![](/images/end.png)


## 流程圖 ：
![](/images/bfs.jpg)
![](/images/dfs.jpg)
## BFS與DFS比較 ：
DFS與BFS大同小異，只是queue換成了stack而已。
舉一個例子來看:

![](/images/example.jpg)

#### BFS : 
要先看完一層目錄後，才會再看下一層。意思就是點進「image」檔後，要先看完「image」檔中下一層的所有檔，也就是會看到「apple」、「pig」兩個檔案。再繼續往下看，點進「apple」檔裡，會看到「red.jpg」、「small.jpg」。接者返回上一頁，點進「pig」檔裡，會看到「fat.jpg」、「cute.jpg」。

#### DFS :
看到「image」檔就會直接點入，首先會看到「apple」檔，再點進去會看到「red.jpg」、「small.jpg」。再返回「image」檔，才會看到有「pig」檔，點進去會看到「fat.jpg」、「cute.jpg」。

#### 結論：
若要在圖形中找出欲到達目標的最少步驟或尋找其中一個連通分支中的所有節點（擴散性），則可採用BFS。若要找出圖形的完整形狀或來儲存未訪問的節點，就可以採用DFS。 





## 參考資料：
https://kopu.chat/2017/09/22/%E5%AF%A6%E4%BD%9Cgraph%E8%88%87dfs%E3%80%81bfs%E8%B5%B0%E8%A8%AA/
https://magiclen.org/dfs-bfs/
https://www.itread01.com/content/1541297601.html
https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/102866/
