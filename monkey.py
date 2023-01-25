#Juan Esteban Acosta López (8952309) 6/08/2022

from sys import stdin

def esPosibleAlcanzarEscalon( alturaEscalones, numeroEscalones, mid ):
    decremento = 0
    for i in range( numeroEscalones ):
        if alturaEscalones[ i ] - decremento < int( mid ):
            decremento = alturaEscalones[ i ]
        elif alturaEscalones[ i ] - decremento == int( mid ):
            mid -= 1
            decremento = alturaEscalones[ i ]
        else:
            return False
    return True

def busquedaBinaria( alturaEscalones, numeroEscalones ):
    low = 0
    high = 10000000
    while high - low > 0.000001:
        mid = ( low + high ) / 2
        if esPosibleAlcanzarEscalon( alturaEscalones, numeroEscalones, mid ):
            high = mid
        else:
            low = mid
    return mid

def main():
    numeroCasosPrueba = int( stdin.readline() )
    for i in range( numeroCasosPrueba ):
        numeroEscalones = int( stdin.readline() )
        alturaEscalones = list( map( int, stdin.readline().strip().split( " " ) ) )
        if numeroEscalones == 1:
            print( f"Case { i + 1 }: { alturaEscalones[ 0 ] }" )
        else:
            print( f"Case { i + 1 }: { round( busquedaBinaria( alturaEscalones, numeroEscalones ) ) }" )
main()