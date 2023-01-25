#Juan Esteban Acosta López (8952309)

#Basado en el codigo de Carlos ramirez de arboles y grafos (DFS modificado) para el uso de este problema

from sys import stdin

def encontrarCaminos( numeroNodos, grafo, visitados, longitudCaminos, respuestas, u, longitudCamino, respuesta ):
    if longitudCamino == longitudCaminos:
        respuestas.append( respuesta )
        return
    visitados[ u ] = True
    for v in range( numeroNodos ):
        if not visitados[ v ]: 
            if grafo[ u ][ v ]:
                if v != u:
                    encontrarCaminos( numeroNodos, grafo, visitados, longitudCaminos, respuestas, v, longitudCamino + 1, respuesta + "," + str( v + 1 ) )
    visitados[ u ] = False

def main():
    separador = " "
    while separador != "":
        numeroNodos, longitudCaminos =  list( map( int, stdin.readline().strip().split( " " ) ) )
        grafo = [ [ 0 for _ in range( 12 ) ] for _ in range( 12 ) ]
        for i in range( numeroNodos ):
            temp = list( map( int, stdin.readline().strip().split( " " ) ) )
            contador = 0
            for j in range( numeroNodos ):
                grafo[ i ][ j ] = temp[ contador ]
                contador += 1
        visitados = [ False for _ in range( numeroNodos + 1 ) ]
        respuestas = []
        encontrarCaminos( numeroNodos, grafo, visitados, longitudCaminos, respuestas, 0, 0, "" )
        if len( respuestas ) != 0:
            for i in range( len( respuestas ) ):
                print( f"(1{ respuestas[ i ] })" )
        else:
            print( f"no walk of length { longitudCaminos }" )
        print()
        separador = stdin.readline()

main()