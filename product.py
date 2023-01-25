#Juan Esteban Acosta López (8952309) 29/09/2022

from sys import stdin

def main():
    linea = stdin.readline().strip()
    while linea != "":
        secuencia = list( map( int, linea.split( " " ) ) )
        while secuencia[ len( secuencia ) - 1 ] != -999999:
            temp = list( map( int, stdin.readline().strip().split( " " ) ) )
            for i in range( len( temp ) ):
                secuencia.append( temp[ i ] )
        maximo = -2 ** 32
        for i in range( len( secuencia ) - 1 ):

            suma = 1
            for j in range( i, len( secuencia ) - 1 ):
                suma *= secuencia[ j ]
            if maximo < suma:
                maximo = suma
        print( maximo )
        linea = stdin.readline().strip()
    
main()