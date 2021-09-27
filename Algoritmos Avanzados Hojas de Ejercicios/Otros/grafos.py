#Importar la libreria collections en especifico la propiedad default
from collections import defaultdict
#Se crea la clase Grafo
class Graph:
    #Constructor de la clase
    def __init__(self,vertices):
        #Inicializa sus atributos
        self.V=vertices
        self.graph=defaultdict(list)

    #Agregar nodo
    def addEdge(self,u,v):
        self.graph[u].append(v)

    #Mostrar los vertices
    def printVertexCover(self):
        #inicializar una lista con valor falso
        visited=[False]*(self.V)
        #Verifixa si los nodos ya fueron visitados anteriormente
        for u in range(self.V):
            if not visited[u]:
                for v in self.graph[u]:
                    if not visited[v]:
                        visited[v]=True
                        visited[u]=False
                        break
        for j in range(self.V):
            if visited[j]:
                print(j,end=" ")
        print()

#Inicializamos la clase con 7 vertices
g=Graph(7)
#Agregar nodos
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(5, 6)
#Mostrar el vertex cover
g.printVertexCover()
