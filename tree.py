from sys import stdin

#Juan Esteban Acosta Lopez - Octubre 2022

colores = 0

def colorear( grafito, numeroHojita, longitudCaminos ):
    global colores
    if len( grafito[ numeroHojita ] ) == 0:
        return 0
    else:
        tamanioColor = -1
        for i in grafito[ numeroHojita ]:
            j = colorear( grafito, i, longitudCaminos )
            tamanioColor = max( j, tamanioColor )
        if tamanioColor == longitudCaminos - 1:
            colores += 1
            rutasMaximas = -1
        else:
            rutasMaximas = tamanioColor + 1
        return rutasMaximas

def main():
    global colores
    linea = stdin.readline().strip()
    while linea != "":
        numeroNodos, numeroLineas, longitudCaminos = list( map( int, linea.split( " " ) ) )
        grafito = [ [  ] for _ in range( numeroNodos ) ]
        for _ in range( numeroLineas ):
            palGrafo = list( map( int, stdin.readline().strip().split( " " ) ) )
            for i in range( 1, len( palGrafo ) ):
                grafito[ palGrafo[ 0 ] ].append( palGrafo[ i ] )
        colorear ( grafito, 0, longitudCaminos )
        print( colores )
        colores = 0
        linea = stdin.readline().strip()

main()