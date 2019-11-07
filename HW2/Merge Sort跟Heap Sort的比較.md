## Heap Sort:
結構以完全二元樹的方法進行排序，可以分成兩種，一是排序的陣列從小到大製作成「最小堆積」(Min Heap），
二是排序的陣列從大到小製作成「最大堆積」(Max Heap)。

## Merge sort:
Merge Sort屬於Divide and Conquer演算法，把數列先分成一半，再將分好的數列切一半，直到每個數列都變成單一元素，
再來進行合併將單一元素兩兩合併，並小的排左邊，大的排右邊，在持續將合併好的數列合併，直到所有數列變成一個大數列。

## 比較圖：
/[](/images/images/photo.png)

由上圖可知，Heap Sort和Merge Sort的best case、average case、worst case都相同。大部分的比較，Heap Sort比Merge Sort快速。
以空間複雜度Extra Space(in-place)相比 Merge Sort為O(n)、Heap Sort為O(1)，在空間上，Heap Sort較快速，因為Heap Sort是以二元樹的概念而來，
不具有空間上的限制。但是Heap Sort的穩定度就沒有Merge Sort好。

