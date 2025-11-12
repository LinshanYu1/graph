import heapq

# every time expanding, prim chooses the edge with the lowest weight

def prim(graph, start_vertex):


    visited = set([start_vertex])
    mst_edges = []
    heap = []


    for neighbor, weight in graph[start_vertex]:
        if neighbor not in visited:
            heapq.heappush(heap,(weight,start_vertex,neighbor))

    while heap and len(visited) < len(heap):
        weight, u, v = heapq.heappop(heap)

        if v not in visited:
            visited.add(v)
            mst_edges.append((u, v,weight))

            for neighbor, w in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(heap,(w,v,neighbor))


    return mst_edges