class Graph:
    def __init__(self):
        self.grafo = {}
    
    def adiciona_node(self, node):
        self.grafo[node] = []
    
    def adiciona_filho(self, node, filho):
        self.grafo[node].append(filho)
    
    def ver_grafo(self):
        return self.grafo


g1 = Graph()
g1.adiciona_node('A')
g1.adiciona_filho('A', 'B')
g1.adiciona_filho('A', 'C')
g1.adiciona_node('B')
g1.adiciona_filho('B', 'A')
g1.adiciona_filho('B', 'D')

print(g1.ver_grafo())