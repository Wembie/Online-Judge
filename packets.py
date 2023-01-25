from sys import stdin

#Juan Esteban Acosta Lopez - Octubre 2022

def main():
    linea = stdin.readline().strip()
    while linea != "0 0 0 0 0 0":
        cajas = list( map( int, linea.split( " " ) ) )
        parcelas = 0
        parcelas += cajas[ 5 ]
        parcelas += cajas[ 4 ]
        cajas[ 0 ] -= 11 * cajas[ 4 ]
        parcelas += cajas[ 3 ]
        cajas[ 1 ] -= 5 * cajas[ 3 ]
        parcelas += cajas[ 2 ] // 4
        if cajas[ 2 ] % 4 == 1:
            cajas[ 1 ] -= 5
            cajas[ 0 ] -= 7
        elif cajas[ 2 ] % 4 == 2:
            cajas[ 1 ] -= 3
            cajas[ 0 ] -= 6
        elif cajas[ 2 ] % 4 == 3:
            cajas[ 1 ] -= 1
            cajas[ 0 ] -= 5
        if cajas[ 2 ] % 4 != 0:
            parcelas += 1
        if cajas[ 1 ] > 0:
            parcelas += cajas[ 1 ] // 9
            if cajas[ 1 ] % 9 > 0:
                parcelas += 1
                cajas[ 0 ] -= 36 - cajas[ 1 ] % 9 * 4
        else:
            cajas[ 0 ] += cajas[ 1 ] * 4
        if cajas[ 0 ] > 0:
            parcelas += cajas[ 0 ] // 36
            if cajas[ 0 ] % 36 > 0:
                parcelas += 1
        print( parcelas )
        linea = stdin.readline().strip()   

main()