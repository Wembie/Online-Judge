from sys import stdin

#Juan Esteban Acosta Lopez - Septiembre

def main():
    numeroCasos = int( stdin.readline() )
    for i in range( 1, numeroCasos + 1 ):
        stdin.readline()
        n, m = list( map( int, stdin.readline().split() ) ) #n -> numero de nodos, m-> numero de aristas
        pesoNodo = list( map( int, stdin.readline().split() ) )
        mejorEleccion = [ 0 for x in range( 1000 ) ]
        for j in range( m ):
            a, b = list( map( int, stdin.readline().split() ) ) #que hay es un borde dirigido de u a v.
            if pesoNodo[ mejorEleccion[ a ] ] < pesoNodo[ b ]: #para saber que mejor camino toma para tener la mayor cantidad de aprendizaje
                mejorEleccion[ a ] = b #y vamos haciendo el mejor camino
        nodo = 0
        sumaNodosVisitados = 0 #Aprendizaje
        while mejorEleccion[ nodo ]: #recorre los nodos hasta que nos de un nodo 0
            nodo = mejorEleccion[ nodo ]
            sumaNodosVisitados += pesoNodo[ nodo ]
        print( f"Case { i }: { sumaNodosVisitados } { nodo }" ) #El nodo represetan donde termina el viaje de la personita :3

main()
