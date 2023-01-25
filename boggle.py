#Juan Esteban Acosta López (8952309)

from sys import stdin


dx = [ -1, 1, 0, 0, -1, -1, 1, 1 ]
dy = [ 0, 0, -1, 1, -1, 1, -1, 1 ]

def boggleBlitz( x, y ):
    global palabra
    global respuestas
    global numeroCaracteres
    global tablero
    if len( palabra ) >= 3:
        respuestas.append( palabra )
    for i in range( 8 ):
        nx = x + dx[ i ]
        ny = y + dy[ i ]
        if nx >= 0 and nx < numeroCaracteres:
            if ny >= 0 and ny < numeroCaracteres:
                if tablero[ nx ][ ny ] > tablero[ x ][ y ]:
                    palabra += tablero[ nx ][ ny ]
                    boggleBlitz( nx, ny )
                    palabra = palabra[ :-1 ]

def main():
    global palabra
    global respuestas
    global numeroCaracteres
    global tablero
    tablero = [ [ None for __ in range( 21 ) ] for _ in range( 21 ) ]
    casos = int( stdin.readline() )
    stdin.readline()
    palabra = ""
    for _ in range( casos ):
        numeroCaracteres = int( stdin.readline() )
        respuestas = []
        for i in range( numeroCaracteres ):
            tablero[ i ] = list( stdin.readline().strip() )
        for i in range( numeroCaracteres ):
            for j in range( numeroCaracteres ):
                palabra += tablero[ i ][ j ]
                boggleBlitz( i, j )
                palabra = palabra[ :-1 ]
        respuestas.sort()
        respuestas.sort( key = lambda x: len(x) )
        impresos = {}
        for i in respuestas:
            try:
                if impresos[ i ]:
                    print( i )
                    impresos[ i ] = True
            except KeyError:
                print( i )
                impresos[ i ] = False
        stdin.readline()

main()