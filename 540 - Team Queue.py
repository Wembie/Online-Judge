#Wembie

from sys import stdin

def main():
    numeroCaso = 1
    numeroEquipos = int( stdin.readline() )
    while numeroEquipos != 0:
        colaAlmuerzo = []
        equiposAux = [ [] for _ in range( numeroEquipos ) ]
        equipos = {}
        for i in range( numeroEquipos ):
            equipo = list( map( int, stdin.readline().strip().split( " " ) ) )[ 1 : ]
            for j in range( len( equipo ) ):
                equipos[ equipo[ j ] ] = i
        comandoCompleto = stdin.readline().strip().split( " " )
        comando = comandoCompleto[ 0 ]
        print( f"Scenario #{ numeroCaso }" )
        while comando != "STOP":
            if comando == "ENQUEUE":
                equipoAEntrar = int( comandoCompleto[ 1 ] )
                if len( equiposAux[ equipos[ equipoAEntrar ] ] ) == 0:
                    colaAlmuerzo.append( equipos[ equipoAEntrar ] )
                equiposAux[ equipos[ equipoAEntrar ] ].append( equipoAEntrar )
            elif comando == "DEQUEUE":
                equipo = colaAlmuerzo[ 0 ]
                print( equiposAux[ equipo ].pop( 0 ) )
                if len( equiposAux[ equipo ] ) == 0:
                   colaAlmuerzo.pop( 0 )
            comandoCompleto = stdin.readline().strip().split( " " )
            comando = comandoCompleto[ 0 ]
        numeroEquipos = int( stdin.readline() )
        numeroCaso += 1
        print()

main()