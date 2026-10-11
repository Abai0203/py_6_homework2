from collections import deque


graph = {
    "Дом": ["Парк", "Остановка"],
    "Парк": ["Дом", "Магазин", "Кафе"],
    "Остановка": ["Дом", "Школа"],
    "Магазин": ["Парк", "Библиотека"],
    "Кафе": ["Парк", "Стадион"],
    "Школа": ["Остановка", "Библиотека"],
    "Библиотека": ["Магазин", "Школа", "Стадион"],
    "Стадион": ["Кафе", "Библиотека"],
}


def breadth_first_search(graph, start, goal):
    queue = deque([start])
    parents = {start: None}
    check_order = []

    while queue:
        current = queue.popleft()
        check_order.append(current)

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in parents:
                parents[neighbor] = current
                queue.append(neighbor)

    path = []
    if goal in parents:
        current = goal
        while current is not None:
            path.append(current)
            current = parents[current]
        path.reverse()

    return check_order, path


if __name__ == "__main__":
    start = "Дом"
    goal = "Стадион"
    order, path = breadth_first_search(graph, start, goal)

    print("Порядок проверки вершин:")
    print(" -> ".join(order))
    print(f"Кратчайший путь от {start} до цели {goal}:")
    print(" -> ".join(path))
