from sys import stdin

#Juan Esteban Acosta Lopez - Octubre

#Basado en el codigo del profe carlitos con implementaciones para que el programa pueda funcionar acorde a este problema

MAX = 1001
calles = [ [ ] for _ in range( MAX ) ] 
low = [ -1 for _ in range( MAX ) ]
visitado = [ 0 for _ in range( MAX ) ]
numeroIntersecciones = None
numeroCalles = None
t = None

def imprimir():
    global numeroIntersecciones, calles
    for i in range( numeroIntersecciones ):
        for j in range( numeroIntersecciones ):
            if calles[ i ][ j ]:
                print( i, j )

def dfsAux( u, v ):
    global t, visitado, numeroIntersecciones, calles, low
    t += 1
    visitado[ v ] = t
    low[ v ] = t
    for i in range( numeroIntersecciones ):
        if calles[ v ][ i ]:
            if not visitado[ i ]:
                dfsAux( v, i )
                low[ v ] = min( low[ v ], low[ i ] )
                if visitado[ v ] >= low[ i ]:
                    calles[ i ][ v ] = 0
                elif u != i:
                    low[ v ] = min( low[ v ], visitado[ i ] )
                    calles[ i ][ v ] = 0

def dfs():
    global numeroIntersecciones, visitado
    for i in range( numeroIntersecciones ):
        if not visitado[ i ]:
            dfsAux( i, i )
    
def main():
    global calles, numeroIntersecciones, numeroCalles, t
    casos = 1
    numeroIntersecciones, numeroCalles = list( map( int, stdin.readline().split() ) )
    while numeroIntersecciones != 0 and numeroCalles != 0:
        print( casos )
        t = 0
        for i in range( numeroIntersecciones + 1 ):
            visitado[ i ] = 0
            low[ i ] = -1
            calles[ i ] = [ 0 for _ in range( numeroCalles + 1 ) ]
        for i in range( numeroCalles ):
            interseccionUno, interseccionDos = list( map( int, stdin.readline().split() ) )
            calles[ interseccionUno ][ interseccionDos ] = 1
            calles[ interseccionDos ][ interseccionUno ] = 1
        dfs() #tarjan
        imprimir()
        print( "#" )
        casos += 1
        numeroIntersecciones, numeroCalles = list( map( int, stdin.readline().split() ) )

main()
