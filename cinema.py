from sys import stdin

#Juan Esteban Acosta Lopez - Octubre 2022

def main():
    linea = stdin.readline().strip()
    while linea != "0 0":
        filas, columnas = list( map( int, linea.split( " " ) ) )
        cine = [ [ False for __ in range( columnas + 1 ) ] for _ in range( filas ) ]
        ubicacionesAmiguixs = [ [ False for __ in range( columnas ) ] for _ in range( filas ) ]
        personasX = int( stdin.readline().strip() )
        for _ in range( personasX ):
            ubicacion, soporte = stdin.readline().strip().split( " " )
            if soporte == "+":
                soporte = 1
            else:
                soporte = 0
            cine[ ord( ubicacion[ 0 ] ) - ord( 'A' ) ][ ( int( ubicacion[ 1: ] ) - 1 ) + soporte ] = True
        amiguixs = int( stdin.readline().strip() ) 
        for _ in range( amiguixs ):
            ubicacion = stdin.readline().strip()
            ubicacionesAmiguixs [ ord( ubicacion[ 0 ] ) - ord( 'A' ) ][ int( ubicacion[ 1: ] ) - 1 ] = True
        sePuede = True
        print(cine,ubicacionesAmiguixs)
        i = 0
        while i < filas and sePuede:
            j = 0
            while j < columnas and sePuede:
                if ubicacionesAmiguixs[ i ][ j ]:
                    if not cine[ i ][ j ]:
                        cine[ i ][ j ] = True
                    elif not cine[ i ][ j + 1 ]:
                        cine[ i ][ j + 1 ] = True
                    else:
                        sePuede = False
                j += 1
            i += 1
        if sePuede:
            print( "YES" )
        else:
            print( "NO" )
        linea = stdin.readline().strip()

main()