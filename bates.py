#Juan Esteban Acosta López (8952309) 10/09/2022

from sys import stdin

def busquedaBinaria( low, lista, x ):
    high = len( lista )
    while low < high:
        mid = ( low + high ) // 2
        if lista[ mid ] <= x:
            low = mid + 1
        else:
            high = mid
    try:
        return lista[ low ] 
    except IndexError:
        return lista[ low + 1 ] 

def main():
    letras = [ [  ] for _ in range( 58 ) ]
    cadena = stdin.readline().strip()
    for i in range( len( cadena ) ):
        letras[ ord( cadena[ i ] ) - ord( 'A' ) ].append( i )
    print( letras )
    numeroConsultas = int( stdin.readline() )
    for _ in range( numeroConsultas ):
        miniCadena = stdin.readline().strip()
        match = []
        for i in range( len( miniCadena ) ):
            if len( match ) == 0:
                matched = busquedaBinaria( 0, letras[ ord( cadena[ i ] ) - ord( 'A' ) ], -1 )
                match.append( matched )
            else:
                if len( letras[ ord( cadena[ i ] ) - ord( 'A' ) ] ) > 1:
                    matched = busquedaBinaria( match[ len( match ) - 1 ], letras[ ord( cadena[ i ] ) - ord( 'A' ) ], match[ len( match ) - 1 ] )
                else:
                    matched = letras[ ord( cadena[ i ] ) - ord( 'A' ) ][ 0 ]
                if matched > match[ len( match ) - 1 ]:
                    match.append( matched )
            print(match)
        if len( match ) == len( miniCadena ):
            print( f"Matched { match[ 0 ] } { match[ len( match ) - 1 ] }" )
        else:
            print( "Not matched" )
main()