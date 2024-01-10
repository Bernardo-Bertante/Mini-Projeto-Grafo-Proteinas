bibtex_reference = '''
@inproceedings{nr-aaai15,
    title = {The Network Data Repository with Interactive Graph Analytics and Visualization},
    author = {Ryan A. Rossi and Nesreen K. Ahmed},
    booktitle = {Proceedings of the Twenty-Ninth AAAI Conference on Artificial Intelligence},
    url = {http://networkrepository.com},
    year = {2015}
}
'''
print(bibtex_reference)

import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

def find_selfLoops ():
    self_loops = list(nx.nodes_with_selfloops(G))
    if self_loops:
        print("O grafo possui laços.")
    else:
        print("O grafo não possui laços.")

def has_cycle_dfs(graph):
    # Encontra ciclos no Grafo 
    visited = set()
    for start_node in graph.nodes():
        if start_node not in visited:
            stack = [(start_node, None)]
            while stack:
                node, parent = stack.pop()
                if node in visited:
                    return True  # Ciclo encontrado
                visited.add(node)
                for neighbor in graph.neighbors(node):
                    if neighbor != parent:
                        stack.append((neighbor, node))
    return False  # Nenhum ciclo encontrado

def count_connectANDvertex():
    # Total de Vértices e Arestas
    total_conexoes = sum(num_connections.values())
    num_totConnections = total_conexoes // 2  # Dividido por 2, já que cada aresta foi contada duas vezes
    print(f"Quantidade de Vértices/Proteínas: {len(adj_list)}\nQuantidade de Arestas/Ligações Protéicas: {num_totConnections}\n") # Quantidade de Vértices/Proteínas
    
def avgDegree():
    # Grau médio dos Vértices
    total_conexoes = sum(num_connections.values())
    num_totConnections = total_conexoes // 2
    avgDegree = num_totConnections / len(adj_list)
    print(f"Grau médio: {avgDegree}\n")    

def find_top_10 ():
    # Encontrar o vértice com mais conexões
    top_10_vertex = sorted(num_connections, key=num_connections.get, reverse=True)[:10]
    top_10_connections = {vertex: num_connections[vertex] for vertex in top_10_vertex}
    
    return top_10_connections

def draw_G (): # Usei essa função somente para gerar os .png enviados no documento
    # Desenhar o grafo
    top_10_labels = {vertex: f"Vértice {vertex}\nConexões: {connections}" for vertex, connections in find_top_10().items()}
    pos = nx.spring_layout(G)  # Define o layout do grafo
    nx.draw(G, pos, with_labels=True, labels= top_10_labels,node_size=300, node_color='skyblue', font_size=10)
    plt.title('Grafo com os Top 10 V!')
    plt.show()

# Carregar o arquivo e processar as conexões
file_path = "amostra-grafo.txt"

adj_list = defaultdict(list)

with open(file_path, 'r') as file:
    lines = file.readlines()[2:]  # Ignorar as duas primeiras linhas do cabeçalho
    for line in lines:
        source, target = map(int, line.split())
        adj_list[source].append(target)
        adj_list[target].append(source)  # Adiciona para arestas bidirecionais

# Criar um grafo a partir da lista de adjacência
G = nx.Graph(adj_list)

# Contagem do número de conexões para cada vértice
num_connections = {vertex: len(neighbors) for vertex, neighbors in adj_list.items()}

count_connectANDvertex()
avgDegree()
find_selfLoops()

if has_cycle_dfs(G):
    print("\nO grafo possui ciclos.\n")
else:
    print("\nO grafo não possui ciclos.\n")

print("Top 10 proteínas com mais ligações:\n")
for vertex, connections in find_top_10().items():
        print(f"Vértice {vertex}: {connections} conexões.")

articulation_points = list(nx.articulation_points(G))

print(f"\nQuantidade de proteínas que funcionam como articulações: {len(articulation_points)} \n")

print(f"Deseja ver todas as {len(articulation_points)} proteínas?")
choise = int(input("1 - SIM\n2 - NÃO\n"))

if (choise == 1):
     print(articulation_points)








