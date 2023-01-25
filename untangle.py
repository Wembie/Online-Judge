#Juan Esteban Acosta López (8952309) 23/10/2022

from sys import stdin

#Tomado de Camilo Rocha

def encontrarIndice( a, low, high, x ):
    while low + 1 != high:
        mid = ( low + high ) // 2
        if a[ mid ] > x:
            high = mid
        else:
            low = mid
    return high

def lis( a ):
    ans = [ a[ 0 ][ 1 ] ]
    for n in range( 1, len( a ) ):
        if ans[ -1 ] <= a[ n ][ 1 ]:
            ans.append( a[ n ][ 1 ] )
        else:
            ans[ encontrarIndice( ans, -1, len( ans ) -1, a[ n ][ 1 ] ) ] = a[ n ][ 1 ]
    return len( ans )

def main():
    numeroCuerdas = int( stdin.readline() )
    while numeroCuerdas != 0:
        cuerdaArriba = list( map( int, stdin.readline().strip().split( " " ) ) )
        cuerdaAbajo = list( map( int, stdin.readline().strip().split( " " ) ) )
        #Hagale Mijo
        listica = []
        for i in range( len( cuerdaArriba ) ):
            listica.append( [cuerdaArriba[ i ], cuerdaAbajo[ i ] ] )
        listica.sort()
        print( lis( listica ), end = ' ' )
        listica.sort( reverse = True )
        print( lis( listica ) )
        numeroCuerdas = int( stdin.readline() )

main()
