## Dijkstra原理：
Dijkstra's Algorithm是一種「每次挑選當前最佳選擇(optimal solution)」的Greedy Algorithm，任意選擇從某一節點出發，與出發點相連結的點開始做選擇，
選擇與出發點相距最短的點作為下一個出發點，就一直反覆挑選出發點，直到所有的出發點都被選擇為止。流程圖有較清楚的動向。

## Kruskal原理：
以邊為基礎，不斷的加入新的不構成環狀的最短邊來構成最小生成樹。我們假設一棵樹有m個節點,n條邊。我們要把m個節點看成是有m個獨立生成樹，並把n條邊安照由小到大
的數據進行排列。在n條中，我們依次取出每一條邊，若邊的兩個節點分別在兩棵樹上，就把它們看成一棵獨立樹，若在同一棵樹上，就忽略，尋找下一個。直到尋找完所有
節點，若所有的小生成樹有組成一條生成樹，那就是我們要找的，若沒有組成則就沒有最小生成樹。
時間複雜度 O(ElogE) 可以改寫成 O(ElogV²) = O(2ElogV) = O(ElogV) 。

## 流程圖：
![](/images/D.png)

## 學習歷程：
















## 參考資料：http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html
## https://zhuanlan.zhihu.com/p/34922624
