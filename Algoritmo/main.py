visitados = []
fila = []

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

def vizinhos(vertices, arestas, vertice):
    vizinhos = []
    
    for _origem, _destino in arestas:
        if _origem == vertice:
            vizinhos.append(_destino)

    return vizinhos

def busca_padrao(vertices, arestas, visitados, fila):
    while fila:
        for vizinho in vizinhos(vertices, arestas, fila[0]):
            if vizinho not in fila and vizinho not in visitados:
                fila.append(vizinho)
        visitados.append(fila[0])
        fila.pop(0)

    print(visitados)

def __main__():
    print(vertices)
    init_vetice = input("Digite por qual vertice deseja iniciar: ")
    fila.append(init_vetice)

    busca_padrao(vertices, arestas, visitados, fila)

__main__()
