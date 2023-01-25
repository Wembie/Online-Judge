#Juan Esteban Acosta López (8952309) 29/09/2022

from sys import stdin

def main():
    numeroCuerdas = int( stdin.readline() )
    while numeroCuerdas != 0:
        cuerdaArriba = list( map( int, stdin.readline().strip().split( " " ) ) )
        cuerdaAbajo = list( map( int, stdin.readline().strip().split( " " ) ) )
        #Hagale Mijo
        numeroCuerdas = int( stdin.readline() )

main()