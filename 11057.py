from sys import stdin

def main():
    numeroLibros = int( stdin.readline() )
    while numeroLibros != '':
        numeroLibros = int( numeroLibros )
        precioLibros = list( map( int, stdin.readline().split() ) )
        dineroDePeter = int( stdin.readline() )
        i = 0
        j = len( precioLibros ) - 1
        caso = None
        precioLibros.sort()
        while i < j :
            if precioLibros[ i ] + precioLibros[ j ] == dineroDePeter:
                caso = [ precioLibros[ i ], precioLibros[ j ] ]
                i += 1
                j -= 1
            elif precioLibros[ i ] + precioLibros[ j ] < dineroDePeter:
                i += 1
            else:
                j -= 1
        print( f"Peter should buy books whose prices are { caso[ 0 ] } and { caso[ 1 ] }.\n" )
        stdin.readline()
        numeroLibros = stdin.readline().strip() 
             
main()
