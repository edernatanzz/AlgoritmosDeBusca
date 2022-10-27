def try_coloring(grafo, num_colors): #mapeia as cores para cada nó
    assert num_colors >= 0, "Numero de cores invalido: " % num_colors
    colors = {}
 
    def neighbors_have_different_colors(nodes, color):
        return all(color != colors.get(n) for n in nodes)
 
    for node, adjacents in grafo.items():
 
        found_color = False
 
        for color in range(num_colors):
            if neighbors_have_different_colors(adjacents, color):
                found_color = True
                colors[node] = color
                break
 
        if not found_color:
            return None
 
    return colors
 
 #recebe um grafo e simplesmente aciona a função try_coloring() 
 #com diferentes valores para o número de cores, até que encontre uma configuração válida
def find_grafo_colors(grafo): 
    for num_colors in range(1, len(grafo)):
        colors = try_coloring(grafo, num_colors)
        if colors:
            return colors