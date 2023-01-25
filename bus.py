#Juan Esteban Acosta López (8952309) 23/10/2022

from sys import stdin

def horasExtrasPorPagar( n, d, r, rutasDia, rutasTarde ):
    paga = 0
    for i in range( n ):
        if rutasDia[ i ] + rutasTarde[ i ] > d:
            paga += ( rutasDia[ i ] + rutasTarde[ i ] - d ) * r
    return paga


def main():
    n, d, r = list( map( int, stdin.readline().strip().split( " " ) ) )
    while n + d + r != 0:
        rutasDia = list( map( int, stdin.readline().strip().split( " " ) ) )
        rutasTarde = list( map( int, stdin.readline().strip().split( " " ) ) )
        rutasDia.sort()
        rutasTarde.sort( reverse = True )
        print( horasExtrasPorPagar( n, d, r, rutasDia, rutasTarde ) )
        n, d, r = list( map( int, stdin.readline().strip().split( " " ) ) )

main()