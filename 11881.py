from sys import stdin

#Juan Esteban Acosta Lopez - Agosto

def binSearchByWembai( cf ):
  low = -1 #Se dice que va desde dicha pos
  hi = 10000 #hasta esta
  while hi - low > 0.000001: #eps = 0.000001
    npv = 0
    mid = ( low + hi ) / 2
    for irr in range( len( cf ) ):
      npv += cf[ irr ] / ( 1 + mid ) ** irr
    if npv > 0: #En el caso de que sea npv mayor a 0 significa que el nuevo low sera el mid y con ello ya dividiremos la lista a la mitad
      low = mid
    else: #y asi como en el npv pero alrevez :D
      hi = mid
  return mid  

def main():
  t = int( stdin.readline() )
  while t != 0:
    cf = list( map( int, stdin.readline().split() ) ) 
    print( "%.2f" % binSearchByWembai( cf ) )
    t = int( stdin.readline() )

main()
