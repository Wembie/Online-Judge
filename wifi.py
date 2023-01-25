from sys import stdin

#Juan Esteban Acosta Lopez - Septiembre 2021

def verificarPuntoAcceso( direccionesCasas, mid ):
    puntoAcceso = 0 #empezamos para saber cuantos puntos de acceso tendra desde la direccionesCasas[ 0 ] + mid hasta la ultima
    cobertura = direccionesCasas[ 0 ] + mid #con ello la covertura va a hacer lo que cubre la casa hasta el mid
    for i in range( len( direccionesCasas ) ): #recorremos la lista de direcciones completa ya que nos toca verificar cada covertura de cada casa y saber donde colocar el internet de Main Street
        if cobertura < direccionesCasas[ i ]: #si la covertura no llega hasta la direccion de la casa[ i ] entonces la nueva covertura sera
            cobertura = direccionesCasas[ i ] + mid #dicha direccion mas el mid
            puntoAcceso += 1 #y por cada vez que se pueda acceder a un punto para la internet le sumamos
    return puntoAcceso

def internetMainStreet( direccionesCasas, puntosAcceso ): #Busqueda Binaria
    #if puntosAcceso == 1:
        #print( f"{ ( direccionesCasas[ len( direccionesCasas ) - 1] - 1 ) / 2 }" ) en algunos casos no tomaba el .5, ya que lo queria hacer lo mas eficiente q pudiera
    #else:
        low = 0 #empezamos el low en 0 ya que seria lo mismo que low = direccionesCasas[ 0 ]
        hi = direccionesCasas[ len( direccionesCasas ) - 1 ] #hacemos que el high sea el ultimo elemento de dicha lista
        while hi - low > 1e-4: #un eps para que sea mas preciso 0.00001
            mid = ( low + hi ) / 2
            if verificarPuntoAcceso( direccionesCasas, mid ) < puntosAcceso: #verificamos cada punto de acceso en la funcion de arriba con los actuales que nos dan
                hi = mid
            else: #lo mismo que la linea 22 pero al revez
                low = mid
        print( int( hi ) / 2 ) #Volvemos un int el high ya que era float y lo dividimos entre 2

def main():
    casos = int( stdin.readline() )
    for i in range( casos ):
        puntosAcceso, numeroCasas = list( map( int, stdin.readline().split() ) ) #n , m
        if puntosAcceso >= numeroCasas: #para mejorar la eficacia del algoritmo si el punto de acceso es mayor o igual al numero total de casas en Main Street siempre va a dar 0.0
            print( "0.0" )
            for j in range( numeroCasas ): #Ignora los inputs ya que si los puntos de accesos es mayor o igual al numero de casos dara 0.0 la salida
                stdin.readline()
        else:
            direccionesCasas = [] #se crea la lista que contiene las direcciones de las casas en Main Street
            for j in range( numeroCasas ):
                direccionesCasas.append( int( stdin.readline() ) ) #se agregan las direcciones de las casas a la lista
            direccionesCasas.sort() #se ordena ya que no nos dicen si el input es desordenado o ordenado etc
            internetMainStreet( direccionesCasas, puntosAcceso )

main()