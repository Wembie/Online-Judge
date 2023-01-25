#Juan Esteban Acosta López (8952309) 20/08/2022

from sys import stdin

def busquedaBinaria( numeros, m ):
    low = 0
    high = len( numeros ) - 1
    while low < high:
        mid = ( low + high ) // 2
        if numeros[ mid ] < m:
            low = mid + 1
        elif numeros[ mid ] == m:
            return numeros[ mid ]
        else:
            if numeros[ mid + 1 ] > m:
                high = mid
            else:
                high = mid - 1
    return numeros[ high ]

def main():
    numeros = []
    i = 0
    while i < 32:
        j = 0
        while j < 32:
            calculo = ( 2 ** i ) * ( 3 ** j )
            numeros.append( calculo )
            j += 1
        i += 1  
    numeros.sort()
    m = int( stdin.readline() )
    while m != 0:
        print( busquedaBinaria( numeros, m ) )
        m = int( stdin.readline() )

main()