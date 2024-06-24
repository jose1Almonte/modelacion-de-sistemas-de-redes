import heapq


def dijkstra(cities, travels, origin_code, destination_code):
    graph = {city.code: {} for city in cities}
    for travel in travels:
        graph[travel.origin][travel.destination] = travel.price
        graph[travel.destination][travel.origin] = travel.price
    
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

def dijkstra_min_cities(cities, travels, origin_code, destination_code):
    graph = {city.code: set() for city in cities}
    for travel in travels:
        graph[travel.origin].add(travel.destination)
        graph[travel.destination].add(travel.origin)  # Añadir para caminos bidireccionales
    
    queue, visited = [(0, origin_code, [])], set()
    while queue:
        (hops, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]

            if node == destination_code:
                return (hops, path)

            for adjacent in graph[node]:
                if adjacent not in visited:
                    heapq.heappush(queue, (hops + 1, adjacent, path))
    return (float("inf"), [])