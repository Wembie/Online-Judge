#include <iostream>
#include <map>
#include <vector>
#include <string.h>
#include <queue>

//Juan Esteban Acosta Lopez - Septiembre

const int MAX = 30;

//Basado en el codigo del profe carlitos con implementaciones para que el programa pueda funcionar acorde a este problema

void busquedaAmplitud( int origen, int destino, int tamanioEnvio, std::vector < int > chinaShippingCompany[ MAX ], int envios[ MAX ], bool visitados[ MAX ] ){
	//Lo que hace memset es colocar un valor en dicha lista, vector etc, hasta un index determinado
	//memset( envios, 0, MAX ); //es como hacer un for desde el primer index hasta el ultimo
	//memset( visitados, false, MAX ); //y con ello ir colocando 0 en cada uno de los index hasta el ultimo osea el MAX
	int i;
	for( i = 0; i < MAX ; i++ ){
		envios[ i ] = 0;
		visitados[ i ] = false;
	}
	std::queue < int > cola;
	cola.push( origen );
	visitados[ origen ] = true;
	while( !cola.empty() ){
		int u;
		u = cola.front();
		cola.pop();
		for( i = 0; i < chinaShippingCompany[ u ].size() ; i++ ){
			int v;
			v = chinaShippingCompany[ u ][ i ]; 
			if( !visitados[ v ] ){	//verifica si en dicho trayecto ya fue visitado o no
				visitados[ v ] = true;
				cola.push( v );
				envios[ v ] = envios[ u ] + 1;
			}
		}
		//para que los envios? con ello verificamos si puede hacer un envio de tal parte a tal otra y asi sucesivamente hasta llegar al destino final (si se puede) y/o para la bfsaux que la hice en una sola
	}
	std::cout << envios[destino];
	if( envios[ destino ] ){ //con ello verifica si el destino es posible y como es en c++ no seria un 0 sino una direccion de memoria con ello es posible
		std::cout << "$" << envios[ destino ] * ( tamanioEnvio * 100 ) << std::endl;
	}
	else{ //si no es una direccion de memoria la cual es el destino y que verifico que no se podria llegar o enviar el envio no seria posible
		std::cout << "NO SHIPMENT POSSIBLE" << std::endl;
	}
}

int main() {
	int casos, i, j, numeroAlmacenes, numeroTramos, numeroSolicitudes, tamanioEnvio;
	std::string codigoAlmacen, origen, destino;
	std::cin >> casos;
	std::cout << "SHIPPING ROUTES OUTPUT" << std::endl;
	for( i = 1; i < casos + 1; i++ ){
		std::map< std::string, int > almacenes;
		std::vector < int > chinaShippingCompany[ 30 ];
		int envios[ MAX ];
		bool visitados[ MAX ];	
		std::cin >> numeroAlmacenes >> numeroTramos >> numeroSolicitudes; //M >> N >> P
		for( j = 0; j < numeroAlmacenes; j++ ){
			std::cin >> codigoAlmacen;
			almacenes[ codigoAlmacen ] = j; //Almacenamos en un diccionario / mapa, para saber dependiendo del codigo que index manejaria en dicho caso
		}
		for( j = 0; j < numeroTramos; j++ ){
			std::cin >> origen >> destino;
			chinaShippingCompany[ almacenes[ origen ] ].push_back( almacenes[ destino ] ); //En cada una de las listas en la posicion de el origen almacenaremos la posicion del destino
			chinaShippingCompany[ almacenes[ destino ] ].push_back( almacenes[ origen ] ); //En cada una de las listas en la posicion de el destino almacenaremos la posicion del origen
			//Gracias a ello podremos usar una busqueda de amplitud ya que tendremos diferentes rutas y con ello calcular el costo
		}
		std::cout << "\nDATA SET  " << i << "\n" << std::endl;
		for( j = 0; j < numeroSolicitudes; j++ ){
			std::cin >> tamanioEnvio >> origen >> destino;
			busquedaAmplitud( almacenes[ origen ], almacenes[ destino ], tamanioEnvio, chinaShippingCompany, envios, visitados ); //bfs
		}	
	}
	std::cout << "\nEND OF OUTPUT" << std::endl;
	return 0;
}
