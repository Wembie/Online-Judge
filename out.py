#Juan Esteban Acosta López (8952309)

from sys import stdin

def verificarPosible( indice, total ):
    global tupla
    global visitados
    global posible
    if posible:
        return
    if indice == 5: 
        if total == 23:
            posible = True
        return
    for i in range( 5 ):
        if not visitados[ i ]:
            if total > 23:
                temp = total
                for j in range( 5 ):
                    if not visitados[ j ]:
                        temp -= tupla[ j ]
                if temp > 23:
                    return 
                else:
                    visitados[ i ] = True
                    verificarPosible( indice + 1, total + tupla[ i ] )
                    verificarPosible( indice + 1, total - tupla[ i ] )
                    verificarPosible( indice + 1, total * tupla[ i ] )
            elif total < 0:
                temp = total
                for j in range( 5 ):
                    if not visitados[ j ]:
                        temp += tupla[ j ]
                if temp < 0:
                    return 
                else:
                    visitados[ i ] = True
                    verificarPosible( indice + 1, total + tupla[ i ] )
                    verificarPosible( indice + 1, total - tupla[ i ] )
                    verificarPosible( indice + 1, total * tupla[ i ] )
            else:
                visitados[ i ] = True
                verificarPosible( indice + 1, total + tupla[ i ] )
                verificarPosible( indice + 1, total - tupla[ i ] )
                verificarPosible( indice + 1, total * tupla[ i ] )
            visitados[ i ] = False

def main():
    global tupla
    global visitados
    global posible
    tupla = list( map( int, stdin.readline().strip().split( " " ) ) )
    while sum( tupla ) != 0:
        posible = False
        if tupla[ 0 ] == 23 and tupla[ 1 ] == 23 and tupla[ 2 ] == 23 and tupla[ 3 ] == 23 and tupla[ 4 ] == 23:
            print( "Possible" ) 
            tupla = list( map( int, stdin.readline().strip().split( " " ) ) )
            continue
        if tupla[ 0 ] % 2 == 0 and tupla[ 1 ] % 2 == 0 and tupla[ 2 ] % 2 == 0 and tupla[ 3 ] % 2 == 0 and tupla[ 4 ] % 2 == 0:
            print( "Impossible" ) 
            tupla = list( map( int, stdin.readline().strip().split( " " ) ) )
            continue
        if tupla[ 0 ] == tupla[ 1 ] and tupla[ 1 ] == tupla[ 2 ] and tupla[ 2 ] == tupla[ 3 ] and tupla[ 3 ] == tupla[ 4 ]:
            print( "Impossible" ) 
            tupla = list( map( int, stdin.readline().strip().split( " " ) ) )
            continue
        for i in range( 5 ):
            visitados = [ False, False, False, False, False ]
            visitados[ i ] = True
            verificarPosible( 1, tupla[ i ] )
            if posible:
                break
        if posible:
            print( "Possible" )
        else:
            print( "Impossible" )
        tupla = list( map( int, stdin.readline().strip().split( " " ) ) )

main()