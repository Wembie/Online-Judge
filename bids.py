#Juan Esteban Acosta López (8952309) 6/08/2022

from sys import stdin

def contarEnojadosProductores( lista, x ): 
    low = 0
    high = len( lista )
    while low < high:
        mid = ( low + high ) // 2
        if lista[ mid ] <= x:
            low = mid + 1
        else:
            high = mid
    return low

def contarEnojadosConsumidores( lista, x ):
    low = 0
    high = len( lista )
    while low < high:
        mid = ( low + high ) // 2
        if lista[ mid ] < x:
            low = mid + 1
        else:
            high = mid
    return low
     
def main():
    numeroCasosPrueba = int( stdin.readline() )
    for _ in range( numeroCasosPrueba ):
        cantidadProductores, cantidadConsumidores = list( map( int, stdin.readline().strip().split( " " ) ) )
        productores = None
        if cantidadProductores >= 1:
            productores = list( map( int, stdin.readline().strip().split( " " ) ) )
        elif cantidadProductores < 1:
            stdin.readline()
        if cantidadConsumidores >= 1:
            consumidores = list( map( int, stdin.readline().strip().split( " " ) ) )
        elif cantidadConsumidores < 1:
            stdin.readline()  
        if cantidadProductores == 0:
            print( "0 0" )
        elif cantidadConsumidores == 0:
            print( f"{ max( productores ) } 0" )
        elif cantidadConsumidores == 1:
            print( f"{ max( productores ) } 1" )
        else:
            productores.sort()
            consumidores.sort()
            awita = productores + consumidores
            awita.append( 0 )
            mejor = [ float( "inf" ), float( "inf" ) ]
            for i in range( len( awita ) ):
                enojadosP = len( productores ) - contarEnojadosProductores( productores, awita[ i ] )
                enojadosC = contarEnojadosConsumidores( consumidores, awita[ i ] )
                enojados = enojadosP + enojadosC
                if mejor[ 0 ] > enojados:
                    mejor[ 0 ] = enojados
                    mejor[ 1 ] = awita[ i ]
                elif mejor[ 0 ] == enojados:
                    if mejor[ 1 ] > awita[ i ]:
                        mejor[ 1 ] = awita[ i ]
            print( f"{ mejor[ 1 ] } { mejor[ 0 ] }" )
        
main()