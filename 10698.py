from sys import stdin

def colocarResultados( equipos, resultadoPartido ):
    for equipo in equipos:
        if equipo[ 1 ] == resultadoPartido[ 0 ]:
            #Puntos
            if int( resultadoPartido[ 1 ] ) > int( resultadoPartido[ 3 ] ):
                equipo[ 2 ] += 3
            elif int( resultadoPartido[ 1 ] ) == int( resultadoPartido[ 3 ] ):
                equipo[ 2 ] += 1
            #Partidos Jugados
            equipo[ 3 ] += 1
            #Goles
            equipo[ 4 ] += int( resultadoPartido[ 1 ] )
            #Goles Encontra
            equipo[ 5 ] += int( resultadoPartido[ 3 ] )
            #Diferencia de Goles
            equipo[ 6 ] = equipo[ 4 ] - equipo[ 5 ]
 
        elif equipo[ 1 ] == resultadoPartido[ 4 ]:
            #Puntos
            if int( resultadoPartido[ 3 ] ) > int( resultadoPartido[ 1 ] ):
                equipo[ 2 ] += 3
            elif int( resultadoPartido[ 3 ] ) == int( resultadoPartido[ 1 ] ):
                equipo[ 2 ] += 1
            #Partidos Jugados
            equipo[ 3 ] += 1
            #Goles
            equipo[ 4 ] += int( resultadoPartido[ 3 ] )
            #Goles Encontra
            equipo[ 5 ] += int( resultadoPartido[ 1 ] )
            #Diferencia de Goles
            equipo[ 6 ] = equipo[ 4 ] - equipo[ 5 ]
                
def main():
    numeroEquipos, numeroPartidos = list( map( int, stdin.readline().split() ) )
    while numeroEquipos != 0 or numeroPartidos != 0:
        equipos = []
        for i in range( numeroEquipos ):
            equipo = []
            equipo.append( 0 ) #Posicion -> 0
            equipo.append( str( stdin.readline().strip() ) ) #Nombre -> 1
            equipo.append( 0 ) #Numero de puntos -> 2
            equipo.append( 0 ) #Numero de juegos jugados -> 3
            equipo.append( 0 ) #Numero de goles hechos -> 4
            equipo.append( 0 ) #Numero de goles encontra -> 5
            equipo.append( 0 ) #Diferencia de goles -> 6
            equipo.append( 0.00 ) #Porcentaje de puntos -> 7
            equipos.append( equipo )
        for i in range( numeroPartidos ): 
            resultadoPartido = str( stdin.readline().strip() ).split()
            #[ "Equipo 1", "Numero", "-", "Numero", "Equipo 2" ]
            #      0          1       2      3          4
            colocarResultados( equipos, resultadoPartido )
        equipos.sort( key = lambda x: ( -x[ 2 ], -x[ 6 ], -x[ 4 ], x[ 1 ].lower() ) )
        posicion = 0
        for i in range( numeroEquipos ):
            if i == 0 or equipos[ i ][ 2 ] != equipos[ i - 1 ][ 2 ] or equipos[ i ][ 6 ] != equipos[ i - 1 ][ 6 ] or equipos[ i ][ 4 ] != equipos[ i - 1 ][ 4 ]:
                posicion += 1
                equipos[ i ][ 0 ] = posicion
                print( "%2d. " % equipos[ i ][ 0 ], end = "" )
            else:
                posicion += 1
                print("    ", end = "" )
            print( "%15s %3d %3d %3d %3d%4d " % ( equipos[ i ][ 1 ], equipos[ i ][ 2 ], equipos[ i ][ 3 ], equipos[ i ][ 4 ], equipos[ i ][ 5 ], equipos[ i ][ 6 ] ), end = "" )
            if equipos[ i ][ 3 ] == 0:
                equipos[ i ][ 7 ] = "N/A"
                print( "%6s" % equipos[ i ][ 7 ] )
            else:
                equipos[ i ][ 7 ] = equipos[ i ][ 2 ] * 100 / ( 3.0 * equipos[ i ][ 3 ] )
                print( "%6.2f" % equipos[ i ][ 7 ] )
        numeroEquipos, numeroPartidos = list( map( int, stdin.readline().split() ) )
        if numeroEquipos != 0:
            print( "" )
main()
