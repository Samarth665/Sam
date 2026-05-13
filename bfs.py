import collections 

def bfs(graph,root):

    queue = collections.deque([root])
    visited = set()

    while queue:

        vertex = queue.popleft()
        print(vertex , end=" ")

        visited.add(vertex)

        for i in graph[vertex]:
            if i not in visited and i not in queue:

                queue.append(i)

if __name__ == "__main__":
    graph = { 'A':['B','C','D'],'B':['E','F','G'],'C':[],'D':['H','I'],'E':[],'F':[],'G':[],'H':[],'I':['J','K'],'J':[],'K':[]  }

    bfs(graph,'A')

            