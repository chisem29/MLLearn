def dfs(hs, start, vis=None) :
    if not vis :
        vis = set()
    vis.add(start)
    for edge in hs[start] - vis:
        if edge not in vis :
            dfs(hs, edge, vis)
    return vis

graph = {
    0 : set([2, 1, 3]),
    2 : set([1, 4]),
    1 : set([4]),
    3 : set([4]),
    4 : set([1, 2, 3])
}

print(dfs(graph, 0)) #получаем все вершины графа