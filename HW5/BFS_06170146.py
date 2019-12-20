from collections import defaultdict 
  
class Graph:
    def __init__(self):       
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  

    def BFS(self, s): 
        queue = [s]
        answer= []
        
        while queue:
            s=queue.pop(0)
            answer.append(s)
            for a in self.graph[s]:
                    if a not in answer:
                        queue.append(a)
        return answer
        
    def DFS(self, s):
        answer = []
        stack = [s]

        while stack:
            s = stack.pop(-1)
            if s not in answer:
                answer.append(s)
                neighbours = self.graph[s]
                for neighbour in neighbours:
                    stack.append(neighbour)
        return answer

        
###參考資料：https://kopu.chat/2017/09/22/%E5%AF%A6%E4%BD%9Cgraph%E8%88%87dfs%E3%80%81bfs%E8%B5%B0%E8%A8%AA/
### https://magiclen.org/dfs-bfs/
### https://www.itread01.com/content/1541297601.html
### https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/102866/
