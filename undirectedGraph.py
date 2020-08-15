from collections import defaultdict 

class Graph:

    def __init__(self,vertices): 
        self.V= vertices
        self.graph = defaultdict(list) 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        self.graph[v].append(u) #for undirected graph
    
    def deleteEdge(self, u,v):
        self.graph[u].remove(v)
        self.graph[v].remove(u) #for undirected graph

    def isReachable(self, s, d): #BFS

        visited =[False]*(self.V) 
        queue=[] 
   
        queue.append(s) 
        visited[s] = True
   
        while queue: 
   
            n = queue.pop(0) 
              
            if n == d: 
                return True
   
            for i in self.graph[n]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True

        return False
   


M, N = map(int, input().split())
g = Graph(N)

edges = []
for _ in range(M):
    a,b = map(int, input().split())
    g.addEdge(a,b)
    edges.append((a,b))

check = []

for i,e in enumerate(edges):
    g.deleteEdge(e[0],e[1])
    if not g.isReachable(e[0],e[1]):
        check.append(e)
    g.addEdge(e[0],e[1])

print({u for v in check for u in v})

  
