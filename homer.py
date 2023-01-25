#Juan Esteban Acosta López (8952309) 28/09/2022

from sys import stdin

def tabHomer( m, n, t, tab ):
    i = 1
    while i < t + 1:
        if i >= m:
            if tab[ i - m ] >= 0:
                tab[ i ] = tab[ i - m ] + 1
        if i >= n:
            if tab[ i - n ] >= 0:
                tab[ i ] = max( tab[ i - n ] + 1, tab[ i ] )
        i += 1

def verificarCerveza( t, tab, m, n ):
    if tab[ t ] >= 0:
        print( tab[ t ] ) 
    else:
        cerveza = 0
        while tab[ t ] == -1:
            cerveza += 1
            t -= 1
        print( tab[ t ], cerveza )
   
def main():
    linea = stdin.readline().strip()
    while linea != "":
        m, n, t = list( map( int, linea.split( " " ) ) )
        tab = [ -1 for _ in range( t + 1 ) ]
        tab[ 0 ] = 0
        tabHomer( m, n, t, tab )
        verificarCerveza( t, tab, m, n )
        linea = stdin.readline().strip()  
        
main()