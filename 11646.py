from sys import stdin
import math

#Juan Esteban Acosta Lopez - Agosto

def biseccionSearchByWemboy( a, b ):
  perimetro = 400
  low = 0
  hi = 1000
  theta = math.atan2( a, b ) #El 2 pa q reciva 2 argumentos y seria el arco tangente de un x, y en radianes que seria y/x
  while hi - low > 0.00000000001: #eps = 0.00000000001
    mid = ( low + hi ) / 2
    largo = mid * math.sin( theta ) * 2 #para obtener el largo seria el mid * el seno de theta * 2
    ancho = mid * math.cos( theta ) * 2 #para obtener el ancho seria el mid * el coseno de theta * 2
    arc = mid * ( math.pi - 2 * theta ) * 2 #para por tener el arc seria 
    if arc + 2 * largo < perimetro: #y el arco + 2 ya que ps son 2 * el largo son menores al perimetro significa
      low = mid #que solo nos serviria los valores del mid al hi
    else:
      hi = mid #lo de arriba x2 pero al revez
  return largo, ancho

def main():
  entrada = stdin.readline()
  casos = 1
  while entrada != "":
    a, b = list( map( int, entrada.split( ":" ) ) ) #a : b se quita el :
    print( f"Case { casos }: ", end = "" ) #end = "" para que el siguiente print sea continuo y no de salto de linea
    largo, ancho = biseccionSearchByWemboy( a, b ) #ya que en python se pueden retornar varias varibales en una funcion aproveche dicho metodo
    print( "%.10f %.10f" % ( largo, ancho ) )
    casos += 1
    entrada = stdin.readline()
  
main()
