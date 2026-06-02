import heapq

def shortest_path(graph, start, end):

    pq = [(0, start)]

    distances = {
        node: float("inf")
        for node in graph
    }

    distances[start] = 0

    previous = {}

    while pq:

        current_distance, current_node = heapq.heappop(pq)

        if current_node == end:
            break

        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance

                previous[neighbor] = current_node

                heapq.heappush(
                    pq,
                    (distance, neighbor)
                )

    path = []

    current = end

    while current != start:

        path.append(current)

        current = previous[current]

    path.append(start)

    path.reverse()

    return {
        "path": path,
        "distance": distances[end]
    }