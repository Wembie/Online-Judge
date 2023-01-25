#Juan Esteban Acosta López (8952309) 20/08/2022

from sys import stdin
from heapq import heappush, heappop

def main():
    numeroCasos = int( stdin.readline() )
    for i in range( numeroCasos ):
        tamanioLista = int( stdin.readline() )
        print( f"Case #{ i + 1 }:")
        if tamanioLista == 1:
            stdin.readline()
            print( "1" )
        else:
            lista = []
            for _ in range( tamanioLista ):
                candidato = list( map( int, stdin.readline().strip().split( " " ) ) )
                if len( lista ) == 0:
                    heappush( lista, candidato )
                    #lista.append( candidato )
                else:
                    #print("AWA Candidato", candidato, "Lista[0]", lista[0], candidato[ 0 ] < lista[ 0 ][ 0 ] and candidato[ 1 ] <= lista[ 0 ][ 1 ], candidato[ 0 ] <= lista[ 0 ][ 0 ] and candidato[ 1 ] < lista[ 0 ][ 1 ])
                    if ( candidato[ 0 ] < lista[ 0 ][ 0 ] and candidato[ 1 ] <= lista[ 0 ][ 1 ] ) or ( candidato[ 0 ] <= lista[ 0 ][ 0 ] and candidato[ 1 ] < lista[ 0 ][ 1 ] ):
                        #print(lista)
                        lista = [ candidato ]
                    elif candidato[ 0 ] == lista[ 0 ][ 0 ] and candidato[ 1 ] == lista[ 0 ][ 1 ]:
                        heappush( lista, candidato )
                    else:
                        for j in range( len( lista.copy() ) ):
                            #print("Candidato", candidato, "Lista[i]", lista[j])
                            if candidato in lista:
                                heappush( lista, candidato )
                                #lista.append( candidato )
                                break
                            elif ( candidato[ 0 ] < lista[ j ][ 0 ] or candidato[ 1 ] <= lista[ j ][ 1 ] ) and ( candidato[ 0 ] <= lista[ j ][ 0 ] or candidato[ 1 ] < lista[ j ][ 1 ] ):
                                heappush( lista, candidato )
                                #lista.append( candidato )
                                break
                    #print(lista)
                print( len( lista ) )
        print()

main()