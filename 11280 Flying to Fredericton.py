#Juan Esteban Acosta Lopez - 21/11/2021

#Basado en el codigo de Carlos con sus respectivos cambios para el uso del problema

from sys import stdin

INF = float( 'inf' )
MAX = 1000

def bellmanFord():
    costo[ 'Calgary' ] = 0
    for i in range( 1, numeroCiudades ):
        for u in ciudades:
            for j in range( len( vuelos[ u ] ) ):
                v = vuelos[ u ][ j ][ 0 ]
                if costo[ v ] > costo[ u ] + vuelos[ u ][ j ][ 1 ]:
                    costo[ v ] = costo[ u ] + vuelos[ u ][ j ][ 1 ]
        cotizacion.append( costo[ 'Fredericton' ] )

def main():
    global numeroCiudades, ciudades, costo, vuelos, cotizacion
    numeroEscenarios = int( stdin.readline() )
    for i in range( numeroEscenarios ):
        stdin.readline()
        numeroCiudades = int( stdin.readline() )
        vuelos = {}
        costo = {}
        cotizacion = []
        ciudades = []
        for j in range( numeroCiudades ):
            ciudad = stdin.readline().strip()
            ciudades.append( ciudad )
            vuelos[ ciudad ] = []
            costo[ ciudad ] = INF
        numeroVuelosDisponibles = int( stdin.readline() )
        for j in range( numeroVuelosDisponibles ):
            origen, destino, dinero = list( map( str, stdin.readline().split() ) )
            vuelos[ origen ].append( [ destino, int( dinero ) ] )
        ciudades.reverse()
        bellmanFord()
        print( f"Scenario #{ i + 1 }" )
        escalas = list( map( int, stdin.readline().split() ) )[ 1: ]
        for j in range( len( escalas ) ):
            escala = escalas[ j ]
            try:
                if cotizacion[ escala ] == INF:
                    print( "No satisfactory flights" )
                else:
                    print( f"Total cost of flight(s) is ${ cotizacion[ escala ] }" )
            except IndexError:
                print( "No satisfactory flights" )
        if i < numeroEscenarios - 1:
            print(  )
        
main()