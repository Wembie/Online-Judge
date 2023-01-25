#Juan Esteban Acosta López (8952309)

#Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali, los valores éticos y la integri-dad son tan importantes como la excelencia académica. En este curso se espera que los estudiantes se comporten ética y honestamente, con los más altos niveles de integridad escolar. En particular, se asume que cada estudiante adopta el siguiente código de honor: Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo a seguir los más altos estándares de integridad académica. Integridad académica se refiere a ser honesto, dar crédito a quien lo merece y respetar el trabajo de los demás. Por eso es importante evitar plagiar, engañar, ‘hacer trampa’, etc. En particular, el acto de entregar un programa de computador ajeno como propio constituye un acto de plagio; cambiar el nombre de las variables, agregar o eliminar comentarios y reorganizar comandos no cambia el hecho de que se está copiando el programa de alguien más. Para más detalles consultar el Reglamento de Estudiantes, Sección VI.

from sys import stdin
from collections import deque

#Complejidad Temporal: O( n^2 + c )
#Complejidad Espacial: O( n )

def prove( groupSizes, mem, memPositionFirst, n, l, firstPosition ):
    #Lo que hace esta funcion es ver cuantas personas caben en una vuelta desde el grupo ke esta en la posicion 0 en la cola y las va agregando en la memoria para no repetir dicho proceso y modifica la posicion del grupo que estuvo de primero la primera vez

    #groupSizes: -> Queue[ 0 .. N ] -> cola que contiene los tamaños de todos los grupos
    #mem: -> List[ 0 .. N ] -> lista de tuplas donde se guardan ( cuantas personas pueden entrar si dicho grupo esta de primero, posicion de que grupo va a quedar de primero )
    #memPositionFirst: -> Entero -> Es la posicion de un grupo que esta primero en la cola en cada interacion 
    #n: -> Entero -> son la cantidad de grupos que hay en la cola
    #l: -> Entero -> la cantidad de personas ke caben en la montaña rusa
    #firstPosition: -> Entero -> Es la posicion del primer grupo que entro en la cola por la primera vez
    
    #Retorna los valores de la cantidad de personas que pasaron, la posicion del primero de la cola de la primera, la posicion en el cual esta el primero en cada interacion y la cola directamente para seguir usandolo y con ello ir cambiando su valor respectivo
    first = 0
    coutingPeople = 0
    countingGroup = 0
    while coutingPeople + first <= l and countingGroup < n:
        countingGroup += 1
        firstPosition -= 1
        if firstPosition == -1:
            firstPosition = n - 1
        first = groupSizes.popleft()
        coutingPeople += first
        groupSizes.append( first )
        first = groupSizes[ 0 ] 
    mem[ memPositionFirst ] = coutingPeople, ( memPositionFirst + countingGroup ) % n #Si en el caso de que pase no se pase de n: memPositionFirst + countingGroup, quedaria igual si no se le resta n
    return coutingPeople, firstPosition, memPositionFirst, groupSizes

def totalEarnings( l, c, n, groupSizes, mem ):
    #Lo que va a hacer esta funcion es saber cuanto fue la ganancia total de todo el dinero es decir los dirhams totales.

    #l: -> Entero -> la cantidad de personas ke caben en la montaña rusa
    #c: -> Entero -> la cantidad de viajes que puede hacer el vagón
    #n: -> Entero -> son la cantidad de grupos que hay en la cola
    #groupSizes: -> Queue[ 0 .. N ] -> cola que contiene los tamaños de todos los grupos
    #mem: -> List[ 0 .. N ] -> lista de tuplas donde se guardan ( cuantas personas pueden entrar si dicho grupo esta de primero, posicion de que grupo va a quedar de primero )

    #Retona la cantidad total de dirhams del dia, dejando pasar la mayor cantidad de personas posibles en cada viaje
    money = 0
    firstPosition = 0
    memPositionFirst = 0
    for _ in range( c ):
        if firstPosition != 0:
            memPositionFirst = n - firstPosition
        else:
            memPositionFirst = 0
        if mem[ memPositionFirst ] == None:
            coutingPeople, firstPosition, memPositionFirst, groupSizes = prove( groupSizes, mem, memPositionFirst, n, l, firstPosition )
        else:
            coutingPeople = mem[ memPositionFirst ][ 0 ]
            firstPosition = n - mem[ memPositionFirst ][ 1 ]
        money += coutingPeople
    return money

def main():
    #Lo que va a hacer esta funcion es leer los datos, inicializar algunas varias como tenemos la de mem List[ 0 .. N ] y rellenamos con los valores datos la cantidad de grupos con sus respectivos tamaños

    #No recibe ningun dato ya que es el main

    #Luego de ello se llama a la funcion totalEarnings() con sus respectivos parametros ( l, c, n, groupSizes, mem ) y se imprime la cantidad de dinero ganado en el dia
    l, c, n = list( map( int, stdin.readline().strip().split( " " ) ) )
    mem = [ None for _ in range( n ) ]
    groupSizes = deque()
    for _ in range( n ):
        groupSizes.append( int( stdin.readline() ) )
    print( totalEarnings( l, c, n, groupSizes, mem ) )

main()