class Grpah:
    def __init__(self, size) -> None:
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v, weight)-> None:
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            # self.adj_matrix[v][u] = weight
    
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def dijkistra(self, starting_vertex_data):
        start_vertex = self.vertex_data.index(starting_vertex_data)
        distances = [float('inf')] * self.size
        predecesors = [None] * self.size
        distances[start_vertex] = 0

        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None 
            for i in range(self.size):
                if  not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i
            if u is None:
                break
            visited[u] = True
            
            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt
                        predecesors[v] = u
        return distances, predecesors

    def get_path(self, predecesors, start_vertex, end_vertex):
        path = []
        current = self.vertex_data.index(end_vertex)
        while current is not None:
            path.insert(0,self.vertex_data[current])
            current = predecesors[current]
            if current == self.vertex_data.index(start_vertex):
                path.insert(0, start_vertex)
        return '->'.join(path)

g = Grpah(7)

g.add_vertex_data(0,'A')
g.add_vertex_data(1,'B')
g.add_vertex_data(2,'C')
g.add_vertex_data(3,'D')
g.add_vertex_data(4,'E')
g.add_vertex_data(5,'F')
g.add_vertex_data(6,'G')

g.add_edge(3, 0, 4) # D - A, weight 5
g.add_edge(3, 4, 2) # D - E, weight 2
g.add_edge(0, 2, 3) # A - C, weight 3
g.add_edge(0, 4, 4) # A - E, weight 4
g.add_edge(4, 2, 4) # E - C, weight 4
g.add_edge(4, 6, 5) # A - E, weight 5
g.add_edge(4, 6, 5) # A - G, weight 5
g.add_edge(2, 5, 5) # A - F, weight 5
g.add_edge(2, 1, 2) # C - B, weight 2
g.add_edge(1, 5, 2) # B - F, weight 2
g.add_edge(6, 5, 5) # B - F, weight 5

distances , pred= g.dijkistra("D")
print(pred)
for i, d in enumerate(distances):
    path = g.get_path(pred, 'D',g.vertex_data[i])
    print(f"{path}, Distance: {d}")
