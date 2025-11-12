import heapq

# priority queue store every edge (weight, edge_start, edge_end)
# support condition that some edges have been choosed
def kruskal(graph, choosed_edges):

    #TODO
    visited = set()
    mst_edges = []
    pq = []
    notIn = False

    for (start, end) in choosed_edges:
        notIn = False
        if graph[start] is not None:
            visited.add(start)
            notIn = True
        if graph[end] is not None:
            visited.add(end)
            notIn = True
        if notIn is False:
            mst_edges.append((start, end))

    for node in graph:
        for nb, weight in graph[node]:
            if nb not in visited:
