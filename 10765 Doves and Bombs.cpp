#include <iostream>
#include <vector>
#include <algorithm>

//Juan Esteban Acosta Lopez - Octubre

//Basado en el codigo del profe carlitos con implementaciones para que el programa pueda funcionar acorde a este problema

const int MAX = 10001;

std::vector< std::vector< int > > ferrocarriles( MAX );
int visitado[ MAX ];
int low[ MAX ];
int padre[ MAX ];
int hijos[ MAX ];
int t, numeroEstaciones;

void apAux( int v ){
	int i;
	low[ v ] = visitado[ v ] = t++;
	for( i = 0; i < ferrocarriles[ v ].size(); i++ ){
    	int w = ferrocarriles[ v ][ i ];
    	if( visitado[ w ] == -1 ){
	    	padre[ w ] = v;
	    	apAux( w );
			low[ v ] = std::min( low[ v ], low[ w ] );
			//verificar si es un punto de articulacion
			if( low[ w ] >= visitado[ v ] ){
				hijos[ v ]++;
			}
    	}
    	else if( w != padre[ v ] ){
    		low[ v ] = std::min( low[ v ], visitado[ w ] );
		}
	}
}

void ap(){
	int i;
	for( i = 0; i < numeroEstaciones; i++ ){
    	low[ i ] = visitado[ i ] = padre[ i ] = -1;
	}
	for( i = 0; i < numeroEstaciones; i++ )
    	if( visitado[ i ] == -1 ){
			apAux( i );
		} 		
}

bool comparador( std::pair< int, int > primero, std::pair< int, int > segundo ){
	if( primero.second == segundo.second ){
        return primero.first < segundo.first;
    }
    else{
        return primero.second > segundo.second;
    }
}

int main() {
	int numeroEstacionesBOOM;
	while( std::cin >> numeroEstaciones >> numeroEstacionesBOOM && numeroEstaciones != 0 && numeroEstacionesBOOM != 0 ){
		int x, y, i, j;
		for( i = 0; i < numeroEstaciones; i++ ){
			ferrocarriles[ i ].clear();
		}	
		while( std::cin >> x >> y, x + y > 0 ){
			ferrocarriles[ x ].push_back( y );
			ferrocarriles[ y ].push_back( x );
		}
		ap();	
		std::vector< std::pair< int, int > > posibleBOOM;
		hijos[ 0 ]--;
		for( i = 0; i < numeroEstaciones; i++ ){
			posibleBOOM.push_back( std::pair< int, int > ( i, hijos[ i ] ) );
		}	
		std::sort( posibleBOOM.begin(), posibleBOOM.end(), comparador );
		i = 0;
		for( std::vector< std::pair< int, int > > :: iterator it = posibleBOOM.begin(); it != posibleBOOM.end() && i < numeroEstacionesBOOM; it++, i++ ){
			std::cout << it->first << " " << it->second + 1 << std::endl;
		}
		std::cout << "\n";
	}
	return 0;
}