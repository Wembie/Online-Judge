from sys import stdin
from heapq import heappush, heappop
                
def main():
    numeroCasos = int( stdin.readline() )
    while numeroCasos != 0:
        frecuencia, m  = list( map( int, stdin.readline().split() ) )
        medicamentos = []
        numeros = {}
        for i in range( frecuencia ):
            nombre, numero  = list( map( str, stdin.readline().split() ) )
            heappush( medicamentos, [ int( numero ), i,  nombre ] )
            numeros[ nombre ] = int( numero )
        for i in range( m ):
            temporal = heappop( medicamentos )
            print( f"{temporal[ 0 ] } { temporal[ 2 ] }" )
            temporal[ 0 ] += numeros[ temporal[ 2 ] ] 
            heappush( medicamentos, temporal )
        numeroCasos -= 1
        
main()
