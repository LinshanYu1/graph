import heapq


def dijkstra(graph, start, end):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}

    # priority queue stores (current node, current distance )
    pq = [(0, start)]
    visited = set()

    while pq:
        node, distance = heapq.heappop(pq)

        if node == end :
            break
        if distance > distances[node]:
            continue
        for neighbor, weight in graph[node].items():
            if neighbor in visited:
                continue

            nb_distance = distance + weight
            if nb_distance < distances[neighbor]:
                distances[neighbor] = nb_distance
                previous[neighbor] = node
                heapq.heappush(pq, (nb_distance,neighbor))
        visited.add(node)

    path = []
    node = end
    while node is not None:
        path.insert(0, node)
        node = previous[node]

    return distances[end], path
