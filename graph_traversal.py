from grapth_tree import *
from queue import Queue
import numpy


def breadth_first(graph, start=0):
    queue = Queue()
    queue.put(start)

    visited = numpy.full((graph.num_vertices, ), False, dtype=bool)

    while not queue.empty():
        vertex = queue.get()

        if visited[vertex]:
            continue

        print("Visited: ", vertex)
        visited[vertex] = True

        for v in graph.get_adjacent_vertices(vertex):
            if not visited[v]:
                queue.put(v)


adjacency_matrix_graph  = AdjacenctMatrixGraph(9)
adjacency_matrix_graph.add_edge(0, 1)
adjacency_matrix_graph.add_edge(0, 2)
adjacency_matrix_graph.add_edge(2, 5)
adjacency_matrix_graph.add_edge(2, 4)
adjacency_matrix_graph.add_edge(2, 3)
adjacency_matrix_graph.add_edge(1, 5)
adjacency_matrix_graph.add_edge(5, 6)
adjacency_matrix_graph.add_edge(7, 3)
adjacency_matrix_graph.add_edge(3, 4)
adjacency_matrix_graph.add_edge(2, 5)
adjacency_matrix_graph.show()
print("")

print("Breadth first Traversal of a Graph: ")
breadth_first(adjacency_matrix_graph, 2)
print("")


def depth_first(graph, visited, current=0):
    if visited[current]:
        return

    visited[current] = True

    print("Visited: ", current)

    for vertex in graph.get_adjacent_vertices(current):
        depth_first(graph, visited, vertex)


print("Depth first Traversal of a Graph: ")
visited = numpy.full((adjacency_matrix_graph.num_vertices, ), False, dtype=bool)
depth_first(adjacency_matrix_graph, visited)
print("")
