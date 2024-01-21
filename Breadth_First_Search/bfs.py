def enqueue(queue, data):
    queue.append(data)
    return len(queue)


def dequeue(queue):
    try:
        return queue.pop(0)
    except IndexError as error:
        print(f"{error} is not possible")


def breadth_first(graph, root):
    queue = []
    visited_nodes = []
    queue.append(root)
    visited_nodes.append(root)
    current_node = root

    while len(queue) > 0:
        current_node = dequeue(queue)
        adj_nodes = graph[current_node]
        remaining_elements = sorted(set(adj_nodes) - set(visited_nodes))

        if len(remaining_elements) > 0:
            for element in remaining_elements:
                visited_nodes.append(element)
                enqueue(queue, element)

    return visited_nodes


# Example usage:
graph = dict()

graph["A"] = ["B", "G", "D"]
graph["B"] = ["A", "F", "E"]
graph["C"] = ["F", "H"]
graph["D"] = ["F", "A"]
graph["E"] = ["B", "G"]
graph["F"] = ["B", "D", "C"]
graph["G"] = ["A", "E"]
graph["H"] = ["C"]

result = breadth_first(graph, "A")
print(result)
