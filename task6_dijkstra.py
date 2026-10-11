import heapq

graph = {
    "Дом": {"Остановка 1": 4, "Парк": 2},
    "Парк": {"Дом": 2, "Остановка 1": 1, "Площадь": 7},
    "Остановка 1": {"Дом": 4, "Парк": 1, "Площадь": 3, "Остановка 2": 6},
    "Площадь": {"Парк": 7, "Остановка 1": 3, "Остановка 2": 2, "Колледж": 10},
    "Остановка 2": {"Остановка 1": 6, "Площадь": 2, "Колледж": 3},
    "Колледж": {"Площадь": 10, "Остановка 2": 3},
}


def dijkstra(graph, start, finish):
    distances = {vertex: float("inf") for vertex in graph}
    parents = {vertex: None for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        if current_vertex == finish:
            break

        for neighbor, travel_time in graph[current_vertex].items():
            new_distance = current_distance + travel_time

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parents[neighbor] = current_vertex
                heapq.heappush(priority_queue, (new_distance, neighbor))

    path = []
    current = finish
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()

    if distances[finish] == float("inf"):
        return [], float("inf")

    return path, distances[finish]


if __name__ == "__main__":
    start = "Дом"
    finish = "Колледж"
    path, total_time = dijkstra(graph, start, finish)

    if path:
        print("Самый быстрый маршрут:")
        print(" -> ".join(path))
        print(f"Общее время: {total_time} минут")
    else:
        print("Маршрут не найден")
