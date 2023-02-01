#Wembie

from sys import stdin

def main():
    numeroCasosPrueba = int( stdin.readline() )
    for i in range( numeroCasosPrueba ):
        numeroAmigos = int( stdin.readline() )
        estampasAmigos = []
        repetidos = {}
        cantidadUnicasEstampas = 0
        for _ in range( numeroAmigos ):
            estampas = list( map( int, stdin.readline().split( " " ) ) )[ 1: ]
            repetidosXColumna = []
            for estampita in estampas:
                if estampita in repetidos and not estampita in repetidosXColumna:
                    repetidos[ estampita ] += 1
                else:
                    repetidos[ estampita ] = 1
                    repetidosXColumna.append( estampita )
            estampasAmigos.append( list( set( estampas ) ) )
        for estampita in repetidos:
            if repetidos[ estampita ] == 1:
                cantidadUnicasEstampas += 1
        estampasXAmigo = 0
        cantidadTotal = 0
        print( f"Case { i + 1 }:", end = '' )
        for j in range( numeroAmigos ):
            for k in range( len( estampasAmigos[ j ] ) ):
                if repetidos[ estampasAmigos[ j ][ k ] ] == 1:
                    estampasXAmigo += 1
            ganancia = ( ( estampasXAmigo / cantidadUnicasEstampas ) * 100 ) - cantidadTotal
            cantidadTotal += ganancia
            print( " %.6lf" % ganancia + "%" ,end = '' )
        print() 
main()