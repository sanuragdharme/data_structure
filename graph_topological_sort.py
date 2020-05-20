from grapth_tree import *
from queue import Queue


def topological_sort(graph):
    queue = Queue()
    indegree_map = {}

    for i in range(graph.num_vertices):
        indegree_map[i] = graph.get_indegree(i)

        if indegree_map[i] == 0:
            queue.put(i)

    sorted_list = []

    while not queue.empty():
        vertex = queue.get()

        sorted_list.append(vertex)

        for v in graph.get_adjacent_vertices(vertex):
            indegree_map[v] = indegree_map[v] - 1

            if indegree_map[v] == 0:
                queue.put(v)

    if len(sorted_list) != graph.num_vertices:
        raise ValueError("This graph has a cycle")

    print(sorted_list)


adjacency_matrix_graph = AdjacenctMatrixGraph(9, directed=True)
adjacency_matrix_graph.add_edge(0, 1)
adjacency_matrix_graph.add_edge(0, 2)
adjacency_matrix_graph.add_edge(2, 5)
adjacency_matrix_graph.add_edge(2, 4)
adjacency_matrix_graph.add_edge(2, 3)
adjacency_matrix_graph.add_edge(1, 5)
adjacency_matrix_graph.add_edge(5, 6)
adjacency_matrix_graph.add_edge(7, 3)
adjacency_matrix_graph.add_edge(3, 4)
adjacency_matrix_graph.add_edge(7, 8)

topological_sort(adjacency_matrix_graph)
print("")
