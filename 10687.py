from sys import stdin
from collections import deque

#Juan Esteban Acosta Lopez - Septiembre

MAX = 1000
listaAdj = []

def main():
    global numeroPares
    numeroPares = int( stdin.readline() ) #N
    while numeroPares != 0:
        estaciones = []
        listaPares = list( map( int, stdin.readline().split() ) ) 
        i = 0
        while i < numeroPares + numeroPares:
            estaciones.append( [ listaPares[ i ], listaPares[ i + 1 ] ] )
            i += 2
        numeroPares = int( stdin.readline() )
        
main()