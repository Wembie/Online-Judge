#Juan Esteban Acosta López (8952309) 23/10/2022

from sys import stdin

#Tomado de Camilo Rocha

def msedtab( A, B ):
    M, N = len( A ), len( B )
    tab = [ [ None for _ in range( N + 1 ) ] for _ in range( M + 1 ) ]
    for n in range( N + 1 ): 
        tab[ 0 ][ n ] = n
    for m in range( M + 1 ): 
        tab[ m ][ 0 ] = m
    m, n = 1, 1
    while m != M + 1:
        if n == N + 1:
            m, n = m + 1, 1
        else:
            if A[ m - 1 ] == B[ n - 1 ]:
                tab[ m ][ n ] = tab[ m - 1 ][ n - 1 ]
            else:
                tab[ m ][ n ] = 1 + min( tab[ m - 1 ][ n - 1 ], min( tab[ m - 1 ][ n ], tab[ m ][ n - 1 ] ) )
            n += 1
    return tab[ M ][ N ]

def main():
    linea = stdin.readline().strip().split( " " )
    while len( linea ) != 1 or linea[ 0 ] != '':
        linea2 = stdin.readline().strip().split( " " )
        print( msedtab( linea[ 1 ], linea2[ 1 ] ) )
        linea = stdin.readline().strip().split( " " )
main()