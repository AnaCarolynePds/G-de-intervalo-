import networkx as nx
import matplotlib.pyplot as plt


def eh_tripla(G):
    """
    Verifica se o grafo possui uma tripla asteroidal e
    Se encontrar uma tripla asteroidal, retorna Nao é de intervalo'.
    """
    vertices = list(G.nodes())
    
    # Verifica todas as combinações de três vértices no grafo G
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            for k in range(j + 1, len(vertices)):
                u, v, w = vertices[i], vertices[j], vertices[k]
                
                # Remove os vizinhos do vértice w
                vizinhos_w = set(G.neighbors(w))
                subgraph_without_w = G.copy()
                subgraph_without_w.remove_nodes_from(vizinhos_w)
                if u in subgraph_without_w and v in subgraph_without_w:
                    caminho_uv_sem_w = nx.has_path(subgraph_without_w, u, v)
                else:
                    caminho_uv_sem_w = False
                
                # Remove os vizinhos do vértice v
                vizinhos_v = set(G.neighbors(v))
                subgraph_without_v = G.copy()
                subgraph_without_v.remove_nodes_from(vizinhos_v)
                if u in subgraph_without_v and w in subgraph_without_v:
                    caminho_uw_sem_v = nx.has_path(subgraph_without_v, u, w)
                else:
                    caminho_uw_sem_v = False
                
                # Remove os vizinhos do vértice u
                vizinhos_u = set(G.neighbors(u))
                subgraph_without_u = G.copy()
                subgraph_without_u.remove_nodes_from(vizinhos_u)
                if v in subgraph_without_u and w in subgraph_without_u:
                    caminho_vw_sem_u = nx.has_path(subgraph_without_u, v, w)
                else:
                    caminho_vw_sem_u = False
                
                # Se todos os caminhos existirem, então é uma tripla asteroidal
                if caminho_uv_sem_w and caminho_uw_sem_v and caminho_vw_sem_u:
                    return "Não é de intervalo. Motivo: contém uma tripla asteroidal."
    
    return None  # Não encontrou tripla asteroidal


def ordem_simplicial(G):
    """
    Verifica se o grafo tem uma ordem simplicial.
    Se tiver, retorna 'É de intervalo', caso contrário, 'Não é de intervalo'.
    """
    try:
        ordem = list(nx.find_cliques(G))
        return "É de intervalo."
    except nx.NetworkXException:
        return "Não é de intervalo. Motivo: não tem uma ordem simplicial."


def ciclo(G):
    """
    Verifica se o grafo possui ciclos ímpares maiores que 3.
    Se encontrar algum, retorna 'Não é de intervalo'.
    """
    for ciclo in nx.cycle_basis(G):
        if len(ciclo) > 3:
            return "Não é de intervalo. Motivo: contém ciclos maiores que 3."
    
    return None  # Não encontrou ciclos ímpares maiores que 3


def cria_grafo():
    """
    Cria um grafo a partir das arestas fornecidas pelo usuário.
    O usuário pode inserir as arestas no formato 'u v' e 
    Pressiona 'Enter' duas vezes finaliza a inserção.
    """
    G = nx.Graph()  # Use nx.DiGraph() se for um grafo direcionado
    print("Insira as arestas do grafo no formato 'u v'. Pressione 'Enter' duas vezes para terminar.")
    
    while True:
        entrada = input("Insira uma aresta: ").strip()
        
        if entrada == '':  # Se o usuário pressionou 'Enter' sem digitar
            entrada = input("Pressione 'Enter' novamente para terminar ou insira uma nova aresta: ").strip()
            if entrada == '':  # Se pressionar 'Enter' duas vezes, termina
                break


        # Tenta processar a entrada como um par de vértices
        try:
            u, v = entrada.split()
            G.add_edge(u, v)  # Adiciona a aresta ao grafo
        except ValueError:
            print("Formato inválido. Insira a aresta no formato 'u v'.")
    
    return G


def exibir_arestas(G):
    """
    Exibe todas as arestas do grafo.
    """
    print("Arestas do grafo:")
    for aresta in G.edges():
        print(aresta)


def desenhar_grafo(G):
    """
    Desenha o grafo usando matplotlib.
    """
    pos = nx.spring_layout(G)  # Layout para o grafo
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray', font_size=10, font_weight='bold')
    plt.title("Visualização do Grafo")
    plt.show()


# Criar o grafo a partir das arestas fornecidas pelo usuário
grafo = cria_grafo()


# Exibir as arestas inseridas
exibir_arestas(grafo)


# Desenhar o grafo
desenhar_grafo(grafo)


# Verificar se o grafo é de intervalo
resultado_tripla = eh_tripla(grafo)
resultado_ordem_simplicial = ordem_simplicial(grafo)
resultado_ciclo = ciclo(grafo)


# Determinar se o grafo é de intervalo e fornecer explicação
if resultado_tripla:
    print(resultado_tripla)
elif resultado_ciclo:
    print(resultado_ciclo)
else:
    print("O grafo é de intervalo. Motivo: Não contém tríplas asteroidal nem ciclos ímpares maiores que 3 e possui uma ordem simplicial.")
