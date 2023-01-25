from sys import stdin

#Juan Esteban Acosta Lopez - Octubre

#Basado en el codigo del profe carlitos con implementaciones para que el programa pueda funcionar acorde a este problema

MAX = 501
caminos = [ [  ] for _ in range( MAX ) ]
visitados = [ True for _ in range( MAX ) ]
maximo = None
numeroCiudades = None
numeroCarreteras = None
ciudades = None

def dfsAux( u ):
	global caminos, visitados, maximo
	contadorCiudades = 0
	for i in range( len( caminos[ u ] ) ):
		v = caminos[ u ][ i ][ 0 ] 
		PPA = caminos[ u ][ i ][ 1 ]
		if visitados[ v ] and PPA == maximo:
			visitados[ v ] = False
			contadorCiudades += dfsAux( v )
	return contadorCiudades + 1

def dfs():
	global visitados, numeroCiudades, ciudades
	for i in range( numeroCiudades ):
		if visitados[ i ]:
			visitados[ i ] = False
			ciudades = max( ciudades, dfsAux( i ) )

def main():
	global caminos, visitados, maximo, numeroCiudades, numeroCarreteras, ciudades
	numeroCiudades, numeroCarreteras = list( map( int, stdin.readline().split() ) )
	while numeroCiudades != 0 and numeroCarreteras != 0:
		maximo = float( '-inf' )
		ciudades = 0
		for i in range( numeroCiudades + 1 ):
			caminos[ i ].clear()
			visitados[ i ] = True
		for i in range( numeroCarreteras ):
			puntoFinalU, puntoFinalV, PPA = list( map( int, stdin.readline().split() ) )
			maximo = max( maximo, PPA )
			if PPA == maximo:
				caminos[ puntoFinalU ].append( [ puntoFinalV, PPA ] )
				caminos[ puntoFinalV ].append( [ puntoFinalU, PPA ] )
		dfs()
		print( ciudades )
		numeroCiudades, numeroCarreteras = list( map( int, stdin.readline().split() ) )

main()