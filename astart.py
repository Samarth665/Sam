import heapq

graph = {

'A':[('B',1),('C',4)],
'B':[('D',3),('E',1)],
'C':[('G',2)],
'D':[],
'E':[('G',2)],
'G':[],

}

hvalues = {
    'A':5,
    'B':3,
    'C':2,
    'D':1,
    'E':1,
    'G':0,
}

def a_star(start, goal):

    g_cost = { node : float('inf') for node in graph}
    g_cost[start] = 0

    print(g_cost) 

    queue = []

    heapq.heappush(queue,(0,start))

    came_from = {}

    while queue:

        current_f_cost , current_node = heapq.heappop(queue)
        print(f"Current_node : {current_node}")

        if current_node == goal :

            path = []

            while current_node in came_from:

                path.append(current_node)
                current_node = came_from[current_node]

            path.append(start)
            path.reverse()
            print(f"Path = {path} \n")
            print(f"Final Cost {g_cost[goal]} ")

            return
        
        for n,w in graph[current_node]:

            g = g_cost[current_node]+w
            h = hvalues[n]
            f = g + h 

            if g < g_cost[n]:
                g_cost[n] = g 
                came_from[n] = current_node
                heapq.heappush(queue,(f,n))           







a_star('A','G')
