import heapq

# ucs ：use priority queue to store the total cost
def ucs(graph, start, end):

    frontier = []
    heapq.heappush(frontier, (0, start, [start])) # total cost, current node, current path
    visited = set()

    while frontier:
        cost, node, path = heapq.heappop(frontier)

        if node in visited:
            continue
        visited.add(node)

        if node == end :
            return cost, path

        for neighbor, weight in graph[node].items():
            if neighbor in visited:
                continue

            total_cost = cost + weight
            heapq.heappush(frontier, (total_cost, neighbor, path + [neighbor]))


    return float('inf'), []
