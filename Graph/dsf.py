from typing import List


def add_edge(adj: List[List[int]], s: int,t:int):
    # Add  edge from Vertex s to t
    adj[s].append(t)
    # Due to undirected graph
    adj[t].append(s)

def dfs_rec(adj:List[List[int]],visited:List[bool], s:int):
    visited[s] = True
    print(s, end=" ")
    for  i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited,i)

def dfs(adj:List[List[int]],s:int):
    visited = [False] * len(adj)
    dfs_rec(adj,visited, s)
def create_grpah():
    adj = [[] for _ in range(5)]
    edges = [[1, 2], [1, 0], [2, 0], [2,3], [2, 4]]
    for e in edges:
        add_edge(adj,e[0],e[1])
    return  adj

graph= create_grpah()
dfs(graph,0)

