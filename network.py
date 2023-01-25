#Juan Esteban Acosta López (8952309) 6/08/2022

#Basado en el implementacion de -> Carlos Ramirez <- sobre conjuntos disyuntos

from sys import stdin

MAX = 20005

p, rango = [ 0 for _ in range( MAX ) ], [ 0 for _ in range( MAX ) ]

def makeSet( v ):
    p[ v ], rango[ v ] = v, 0

def findSet( v ):
    ans = None
    if v == p[ v ]: ans = v
    else:
        ans = findSet( p[ v ] )
        rango[ v ] += rango[ p[ v ] ]
        p[ v ] = ans
    return ans

def unionSet( u, v ):
    p[ u ] = v
    rango[ u ] = abs( u - v ) % 1000
     
def main():
    numeroCasos = int( stdin.readline() )
    for _ in range( numeroCasos ):
        numeroEmpresas = int( stdin.readline() )
        for i in range( 1, numeroEmpresas + 1 ):
            makeSet( i )
        linea = stdin.readline().split()
        while linea[ 0 ] != 'O':
            if linea[ 0 ] == 'I':
                unionSet( int( linea[ 1 ] ), int( linea[ 2 ] ) )
            else:
                findSet( int( linea[ 1 ] ) )
                print( rango[ int( linea[ 1 ] ) ] )
            linea = stdin.readline().split()

main()