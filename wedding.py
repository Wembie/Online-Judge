#Juan Esteban Acosta López (8952309) 29/09/2022

from sys import stdin

def comprar( precios, memoria, cantidadDisponibleDinero, numeroPrendasAComprar, dinero, indice ):
    if dinero < 0:
        return -1
    if indice == numeroPrendasAComprar:
        return cantidadDisponibleDinero - dinero
    if memoria[ dinero ][ indice ] != -1:
        return memoria[ dinero ][ indice ] 
    mejor = float( "-inf" )
    for i in range( precios[ indice ] ):
        mejor = max( comprar( precios, memoria, cantidadDisponibleDinero, numeroPrendasAComprar, dinero - precios[ indice ][ i ], indice + 1 ), mejor )

def main():
    memoria = [ [ -1 for __ in range( 21 ) ] for _ in range( 201 ) ]
    numeroCasosPrueba = int( stdin.readline() )
    for i in range( numeroCasosPrueba ):
        precios = []
        cantidadDisponibleDinero, numeroPrendasAComprar = list( map( int, stdin.readline().strip().split( " " ) ) )
        for j in range( cantidadDisponibleDinero ):
            for k in range( numeroPrendasAComprar ):
                memoria[ j ][ k ] = -1
        #memoria = [ [ -1 for __ in range( numeroPrendasAComprar ) ] for _ in range( cantidadDisponibleDinero ) ]
        for j in range( numeroPrendasAComprar ):
            precios.append( list( map( int, stdin.readline().strip().split( " " ) ) ) )
        print( comprar( precios, memoria, cantidadDisponibleDinero, numeroPrendasAComprar, cantidadDisponibleDinero, 0 ) )

main()