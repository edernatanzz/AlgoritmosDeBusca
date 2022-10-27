from graph_coloring import *
from xmlrpc.client import boolean

arquivo = open('C:\codigosVsCode\phyton\Arconsistencia\grafo.txt', 'r')
print(arquivo.read())
grafo =(arquivo.read())
 
try_coloring(grafo , arquivo.read())
#try_coloring(grafo, 2)
#{'A': 0, 'C': 1, 'B': 1  }
{'0': 1, '1': 1, 'B': 3}
#try_coloring(grafo, 3, 2)
