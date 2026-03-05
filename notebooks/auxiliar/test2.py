heuristic = {
 'Arad': 366,
 'Sibiu': 253,
 'Fagaras': 176,
 'Rimnicu Vilcea': 193,
 'Pitesti': 100,
 'Bucharest': 0
}
graph = {
 'Arad': [('Sibiu', 140), ('Fagaras', 99)],
 'Sibiu': [('Rimnicu Vilcea', 80), ('Fagaras', 99), ('Arad', 140)],
 'Fagaras': [('Sibiu', 99), ('Bucharest', 211), ('Arad', 99)],
 'Rimnicu Vilcea': [('Sibiu', 80), ('Pitesti', 97)],
 'Pitesti': [('Rimnicu Vilcea', 97), ('Bucharest', 101)],
 'Bucharest': []
}
import heapq

def greedy_bfs(start, goal):
 # Step 1: Priority queue sorted by heuristic h(n)
 frontier = [(heuristic[start], start)]
 visited = set()
 path = []
 while frontier:
    hn, node = heapq.heappop(frontier)
 path.append(node) # Step 2: Add node to path
 if node == goal:
    return path
 visited.add(node)
 # Step 3: Add neighbors by h(n)
 for neighbor, _ in graph[node]:
    if neighbor not in visited:
        heapq.heappush(frontier, (heuristic[neighbor], neighbor))
    return None
 


def astar(start, goal):
 # Step 1: Priority queue sorted by f(n) = g(n) + h(n)
 frontier = [(heuristic[start], 0, start, [start])]
 visited = set()
 while frontier:
    fn, gn, node, path = heapq.heappop(frontier)
 if node == goal:
    return path
 visited.add(node)
 # Step 2: Add neighbors with updated cost
 for neighbor, cost in graph[node]:
    if neighbor not in visited:
         g_new = gn + cost
 f_new = g_new + heuristic[neighbor]
 heapq.heappush(frontier, (f_new, g_new, neighbor, path + [neighbor]))
 return None
# Run both algorithms
path_gbfs = greedy_bfs('Arad', 'Bucharest')
path_astar = astar('Arad', 'Bucharest')
print('Greedy BFS path:', path_gbfs)
print('A* path:', path_astar)