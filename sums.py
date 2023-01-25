#Juan Esteban Acosta López (8952309) 3/08/2022

from sys import stdin
from heapq import heappush, heappop
              
def main():
    k = stdin.readline().strip()
    while k != "":
        k = int( k )
        mejores = list( map( int, stdin.readline().strip().split( " " ) ) )
        mejores.sort()
        for _ in range( k - 1 ):
            sumas = []
            siguientes = list( map( int, stdin.readline().strip().split( " " ) ) )
            siguientes.sort()
            for i in range( k ):
                heappush( sumas, ( mejores[ i ] + siguientes[ 0 ], 0 ) )
            indice = 0
            while not len( sumas ) != 0 or indice != k :      
                suma, posicion = heappop( sumas )
                mejores[ indice ] = suma
                indice += 1
                if posicion + 1 < k:
                    heappush( sumas, ( suma - siguientes[ posicion ] + siguientes[ posicion + 1 ], posicion + 1 ) )
        for i in range( k ):
            if i < k - 1:
                print( mejores[ i ], end = " " ) 
            else:
                print( mejores[ i ] )
        k = stdin.readline().strip()
main()