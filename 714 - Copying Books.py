#Wembie

from sys import stdin

def esPosible( mid, libros, cantidadDivisiones ):
    divisiones = 1
    suma = 0
    for i in range( len( libros ) ):
        if suma + libros[ i ] <= mid:
            suma += libros[ i ]
        elif divisiones == cantidadDivisiones or mid < libros[ i ]:
            return False
        else:
            suma = libros[ i ]
            divisiones += 1
    return True

def busquedaBinaria( libros, cantidadDivisiones ):
    low = 0
    high = sum( libros )
    while low + 1 < high:
        mid = ( low + high ) / 2
        if esPosible( mid, libros, cantidadDivisiones ):
            high = mid
        else:
            low = mid
    return max( low, mid, high )

def retornarIndicesLibros( numeroLibros, libros, resultado ):
    indicesLibros = list()
    finalDivision = numeroLibros - 1
    suma = 0
    for i in range( len( libros ) - 1, -1, - 1 ):
        if suma + libros[ i ] <= resultado:
            suma += libros[ i ]
        else:
            indicesLibros.append( [ i + 1, finalDivision ] )
            finalDivision = i
            suma = libros[ i ]
    indicesLibros.append( [ 0, finalDivision ] )
    indicesLibros.sort()
    return indicesLibros, len( indicesLibros )

def main():
    numeroCasos = int( stdin.readline() )
    for _ in range( numeroCasos ):
        numeroLibros, cantidadDivisiones = list( map( int, stdin.readline().split( " " ) ) )
        libros = list( map( int, stdin.readline().split(" ") ) )
        if numeroLibros == cantidadDivisiones:
            for i in range( numeroLibros ):
                if i + 1 >= numeroLibros:
                    print( libros[ i ], end = "" )
                else:
                    print( str( libros[ i ] ) + " / ", end = "" )
        else:
            resultado = busquedaBinaria( libros, cantidadDivisiones )
            indicesLibros, division = retornarIndicesLibros( numeroLibros, libros, resultado )
            for i in range( len( indicesLibros ) ):
                for j in range( indicesLibros[ i ][ 0 ], indicesLibros[ i ][ 1 ] + 1 ):
                    if i == len( indicesLibros ) - 1 and j == indicesLibros[ i ][ 1 ]:
                        print( libros[ j ], end = "" )
                    else:
                        print( str( libros[ j ] ) + " ", end = "" )
                    if indicesLibros[ i ][ 1 ] > j and cantidadDivisiones > division:
                        division += 1
                        print( "/ ", end = "" )
                if len( indicesLibros ) > i + 1:
                    print( "/ ", end = "" )
        print()
                
main()