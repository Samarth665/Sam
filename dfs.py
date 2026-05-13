def dfs(graph,vertex,visited):

    visited.add(vertex)
    print(vertex,end=" ")

    for i in graph[vertex]:
        if i not in visited:

            dfs(graph,i,visited)


if __name__ == "__main__":
    graph = { 'A':['B','C','D'],'B':['E','F','G'],'C':[],'D':['H','I'],'E':[],'F':[],'G':[],'H':[],'I':['J','K'],'J':[],'K':[]  }

    visited = set()
    dfs(graph,'A',visited)