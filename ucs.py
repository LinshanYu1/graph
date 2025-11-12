import heapq

# ucs ：use priority queue to store the total cost
def ucs(graph, start, end):

    frontier = []
    heapq.heappush(frontier, (0, start, [start])) # total cost, current node, current path
    visited = set()
    node_cost = {node: float('inf') for node in graph}
    node_cost[start] = 0

    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if cost > node_cost[node]:
            continue

        if node == end:
            return cost, path


        for neighbor, weight in graph[node].items():
            if neighbor in visited:
                continue

            total_cost = cost + weight
            if total_cost < node_cost[neighbor]:
                node_cost[neighbor] = total_cost
                heapq.heappush(frontier, (total_cost, neighbor, path + [neighbor]))
        visited.add(node)

    return float('inf'), []
