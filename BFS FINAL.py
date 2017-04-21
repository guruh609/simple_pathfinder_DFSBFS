graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (cabang, jalur) = queue.pop(0)
        for next in graph[cabang] - set(jalur):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, jalur + [next]))

#print(list(bfs_paths(graph, 'A', 'F')))

def shortest_bfs(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])

#print(list(dfs_paths(graph, 'A', 'F')))

def shortest_dfs(graph, start, goal,path=None):
    try:
        return next(dfs_paths(graph, start, goal,path=None))
    except StopIteration:
        return None
