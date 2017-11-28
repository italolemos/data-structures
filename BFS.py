# As chaves representam os vértices e a lista os vizinhos do respectivo nó
graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['A', 'B','D'],
    'F': ['C'],
    'G': ['C']
}

# visitar todos os nós do gráfico
def bfs_connectd_component(graph, start, goal):
    # Todos os nos visitados
    explored = []
    # nos a serem visitados
    queue = [[start]]

    # se o inicio é igual ao objetivo
    if start == goal:
        return "That was easy! Start = goal"

    # laço p/ os nós serem visitados
    # Ao final do laço a função retorna todos os nós visitados
    while queue:
        # retira o primeiro nó da fila
        path = queue.pop(0)
        # pega o ultimo nó do caminho
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # verifica todos os vizinhos do nó e construi um novo caminho
            # e coloca na lista       
            for neighbour in neighbours:
                new_path = list(path)
                # print(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # retorna o caminho se o nó vizinho é igual ao objetivo
                if neighbour == goal:
                    return new_path
            # nó marcado como explorado
            explored.append(node)
    
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("
print(bfs_connectd_component(graph, 'D', 'C'))