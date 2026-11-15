vertices = ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8"]
arestas = [
    ["v1", "v2"],
    ["v1", "v3"],
    ["v1", "v6"],
    ["v2", "v1"],
    ["v2", "v3"],
    ["v2", "v4"],
    ["v2", "v6"],
    ["v2", "v7"],
    ["v3", "v1"],
    ["v3", "v2"],
    ["v4", "v2"],
    ["v4", "v5"],
    ["v5", "v4"],
    ["v5", "v6"],
    ["v5", "v8"],
    ["v6", "v1"],
    ["v6", "v2"],
    ["v6", "v5"],
    ["v6", "v7"],
    ["v7", "v2"],
    ["v7", "v6"],
    ["v7", "v8"],
    ["v8", "v5"],
    ["v8", "v7"]
]

def vizinhos(arestas, vertice):
    vizinhos = []
    
    for _origem, _destino in arestas:
        if _origem == vertice:
            vizinhos.append(_destino)

    return vizinhos

# Realiza Busca em Largura apartir de um vertice inicial
def busca_padrao(arestas, inicio):
    visitados = []
    fila = [inicio]

    while fila:
        for vizinho in vizinhos(arestas, fila[0]):
            if vizinho not in fila and vizinho not in visitados:
                fila.append(vizinho)
        visitados.append(fila[0])
        fila.pop(0)

    return visitados

# Realiza busca de menor caminho de vertice inicial a um destino utilizando Busca em Largura
def busca_por_menor_caminho(arestas, inicio, destino):
    visitados = []
    fila = [
        {
            'vertice': inicio,
            'caminho': [inicio]
        }
    ]

    while fila:
        if fila[0]["vertice"] == destino:
            return fila[0]["caminho"]
        
        visitados.append(fila[0]["vertice"])

        for vizinho in vizinhos(arestas, fila[0]["vertice"]):
            if vizinho not in visitados and vizinho not in fila:
                fila.append(
                    {
                        'vertice': vizinho,
                        'caminho': [*fila[0]["caminho"], vizinho]
                    }
                )

        fila.pop(0)
            


def __main__():
    print("## Algoritmo de Busca em Largura ##")
    print("Vertices registrados: ")
    print(vertices)
    inicio = input("Digite por qual vertice deseja iniciar: ")
    destino = input("Digite qual vertice sera o destino: ")

    print("Vertices visitados em ordem de busca: ")
    print(busca_padrao(arestas, inicio))

    print("Caminho mais curto de inicio a destino: ")
    print(busca_por_menor_caminho(arestas, inicio, destino))

__main__()
