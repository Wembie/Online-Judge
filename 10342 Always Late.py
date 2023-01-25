#Juan Esteban Acosta Lopez - 20/11/2021

#Basado en el codigo de Carlos con sus respectivos cambios para el uso del problema

from sys import stdin
from heapq import heappop, heappush

INF = float( 'inf' )
MAX = 105
G = [ [] for i in range( MAX ) ]
d, p = [ [ INF, INF ] for i in range( len( G ) ) ], [ -1 for i in range( len( G ) ) ]

def dijkstra( s, r ):
    global d
    """G is a graph representation in adjacency list format with vertices
       in the set { 0, ..., |V|-1 } and source s is a vertex in G"""
    # dist[u] : "minimum distance detected from source to u
    for i in range( numeroUniones ):
        d[ i ] = [ INF, INF ]
    heap = [ ( 0, s ) ]
    while len( heap ) != 0:
        costo, u = heappop( heap )
        if costo != d[ u ][ 0 ]:
            for v, w in G[ u ]:
                if costo + w < d[ v ][ 1 ]:
                    heappush( heap, ( costo + w, v ) )
            if costo < d[ u ][ 0 ]:
                d[ u ][ 0 ] = costo
            elif costo < d[ u ][ 1 ]:
                d[ u ][ 1 ] = costo
                if u == r: #se me ocurrio dicha forma para que no me diera time limit (Pensando en eficacia :D)
                    return
                
def main():
    global numeroUniones
    linea = stdin.readline()
    caso = 1
    while linea != "":
        numeroUniones, numeroCarreterasBidireccionales = list( map( int, linea.split() ) ) #n r
        for i in range( numeroUniones ):
            G[ i ].clear()
        for i in range( numeroCarreterasBidireccionales ):
            numero1, numero2, longitudCarretera = list( map( int, stdin.readline().split() ) )
            G[ numero1 ].append( ( numero2, longitudCarretera ) )
            G[ numero2 ].append( ( numero1, longitudCarretera ) )
        numeroConsultas = int( stdin.readline() ) #q
        print( f"Set #{ caso }" )
        for i in range( numeroConsultas ):
            u, v = list( map( int, stdin.readline().split() ) )
            dijkstra( u, v )
            if d[ v ][ 1 ] == INF:
                print( "?" )
            else:
                print( f"{ d[ v ][ 1 ] }" )
        stdin.readline()
        linea = stdin.readline()
        caso += 1
        
main()