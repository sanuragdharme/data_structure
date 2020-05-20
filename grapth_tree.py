import abc # Abstract base class
import numpy


class Graph(abc.ABC):
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def remove_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        pass

    @abc.abstractmethod
    def is_adjacent(self, v1, v2):
        pass

    @abc.abstractmethod
    def get_indegree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def show(self):
        pass


class Vertex:
    def __init__(self, id):
        self.id = id
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.id == v:
            raise ValueError(f"The vertex {v} cannot be adjacent to itself")

        self.adjacency_set.add(v)

    def remove_edge(self, v):
        if self.id == v:
            raise ValueError(f"The vertex {v} cannot be adjacent to itself")

        self.adjacency_set.remove(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)

    def is_adjacent(self, v):
        return v in self.adjacency_set


print("Adjacent Set Graph")


class AdjacencySetGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        super(AdjacencySetGraph, self).__init__(num_vertices, directed)

        self.vertex_list = []
        for i in range(num_vertices):
            v = Vertex(i)

            self.vertex_list.append(v)

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f"Vertices {v1} and {v2} are out of bounds")

        if weight != 1:
            raise ValueError("An adjacency set cannot represent edge weights > 1")

        self.vertex_list[v1].add_edge(v2)

        if not self.directed:
            self.vertex_list[v2].add_edge(v1)

    def remove_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f"Vertices {v1} and {v2} are out of bounds")

        self.vertex_list[v1].remove_edge(v2)

        if not self.directed:
            self.vertex_list[v2].remove_edge(v1)

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError(f"Cannot access vertex {v}")

        return self.vertex_list[v].get_adjacent_vertices()

    def is_adjacent(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f"Vertices {v1} and {v2} are out of bounds")

        return self.vertex_list[v1].is_adjacent(v2) or self.vertex_list[v2].is_adjacent(v1)

    def get_indegree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError(f"Cannot access vertex {v}")

        indegree = 0
        for i in range(self.num_vertices):
            if i == v:
                continue
            if v in self.get_adjacent_vertices(i):
                indegree += 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def show(self):
        for i in range(self.num_vertices):
            for j in self.get_adjacent_vertices(i):
                print(i, "-->", j)


adjacency_set_graph = AdjacencySetGraph(4)
adjacency_set_graph.add_edge(0, 1)
adjacency_set_graph.add_edge(0, 3)
adjacency_set_graph.add_edge(1, 3)
adjacency_set_graph.add_edge(3, 2)
adjacency_set_graph.show()
print("")

for i in range(4):
    print("Adjacent to:", i, adjacency_set_graph.get_adjacent_vertices(i))
print("")

for i in range(4):
    print(f"Indegree for vertex {i} is {adjacency_set_graph.get_indegree(i)}")
print("")

adjacency_set_graph.remove_edge(2, 3)
adjacency_set_graph.show()
print("")

for i in range(4):
    print("Adjacent to:", i, adjacency_set_graph.get_adjacent_vertices(i))
print("")

print(adjacency_set_graph.is_adjacent(0, 1))

adjacency_set_graph = AdjacencySetGraph(4, directed=True)
adjacency_set_graph.add_edge(0, 1)
adjacency_set_graph.add_edge(0, 3)
adjacency_set_graph.add_edge(1, 3)
adjacency_set_graph.add_edge(3, 2)
adjacency_set_graph.show()
print("")

for i in range(4):
    print("Adjacent to:", i, adjacency_set_graph.get_adjacent_vertices(i))
print("")

for i in range(4):
    print(f"Indegree for vertex {i} is {adjacency_set_graph.get_indegree(i)}")
print("")

print("Adjacent Matrix Graph")


class AdjacenctMatrixGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        super(AdjacenctMatrixGraph, self).__init__(num_vertices, directed)

        self.matrix = numpy.zeros((num_vertices, num_vertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f"Vertices {v1} and {v2} are out of bounds")

        if weight == 0:
            raise ValueError("Edges cannot have a weight of 0")

        self.matrix[v1][v2] = weight
        if not self.directed:
            self.matrix[v2][v1] = weight

    def remove_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f"Vertices {v1} and {v2} are out of bounds")

        self.matrix[v1][v2] = 0
        if not self.directed:
            self.matrix[v2][v1] = 0

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError(f"Cannot access  vertex {v}")

        adjacent_vertices = []
        for i in range(self.num_vertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def is_adjacent(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f"Vertices {v1} and {v2} are out of bounds")

        return self.matrix[v1][v2] != 0

    def get_indegree(self, v):
        if v < 0 or v >= self.num_vertices:
            raise ValueError(f"Cannot access  vertex {v}")

        indegree = 0
        for i in range(self.num_vertices):
            if self.matrix[i][v] > 0:
                indegree += 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def show(self):
        for i in range(self.num_vertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


adjacency_matrix_graph = AdjacenctMatrixGraph(4)
adjacency_matrix_graph.add_edge(0, 1)
adjacency_matrix_graph.add_edge(0, 3)
adjacency_matrix_graph.add_edge(1, 1)
adjacency_matrix_graph.add_edge(3, 2)
adjacency_matrix_graph.show()

for i in range(4):
    print("Adjacent to:", i, adjacency_matrix_graph.get_adjacent_vertices(i))

adjacency_matrix_graph = AdjacenctMatrixGraph(4, directed=True)
adjacency_matrix_graph.add_edge(0, 1)
adjacency_matrix_graph.add_edge(0, 3)
adjacency_matrix_graph.add_edge(1, 1)
adjacency_matrix_graph.add_edge(3, 2)
adjacency_matrix_graph.show()

for i in range(4):
    print("Adjacent to:", i, adjacency_matrix_graph.get_adjacent_vertices(i))
