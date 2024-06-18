import heapq


def dijkstra(cities, travels, origin_code, destination_code):
    graph = {city.code: {} for city in cities}
    for travel in travels:
        graph[travel.origin][travel.destination] = travel.price
    
    queue, visited = [(0, origin_code, [])], set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]

            if node == destination_code:
                return (cost, path)

            for adjacent in graph[node]:
                if adjacent not in visited:
                    heapq.heappush(queue, (cost + graph[node][adjacent], adjacent, path))
    return (float("inf"), [])