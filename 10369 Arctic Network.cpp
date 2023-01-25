//Juan Esteban Acosta Lopez - 20/11/2021

//Basado en el codigo de Carlos con sus respectivos cambios para el uso del problema

#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
 
typedef std::pair< int, int > ii;

std::vector< int > padre( 500 );
std::vector< std::pair< double, ii > > puestosDeAvanzada;
int rango, casos, canalesPorSatelite, numeroPuestosAvanzados, x[ 500 ], y[ 500 ];

void makeSet( int v ){
	int i;
	for( i = 0; i < v ; i++ ){
		padre[ i ] = i;
	}	
	rango = v;
}

int findSet( int v ){
	if( v == padre[ v ] ){
		return v;
	}
	else{
		padre[ v ] = findSet( padre[ v ] );
		return padre[ v ];
	}	
}

void unionSet( int u, int v, double &transceptores, std::pair< double, ii > puestoAvanzada ) {
	u = findSet( u );
	v = findSet( v );
	if( u != v ){
		transceptores = std::max( transceptores, puestoAvanzada.first );
		padre[ u ] = v;
        rango--;
	}
}
 
int main(){
	std::cin >> casos;
	int caso;
	for( caso = 0; caso < casos; caso++ ){
    	int i, j;
    	double distancia, transceptores;
        puestosDeAvanzada.clear();
        std::cin >> canalesPorSatelite >> numeroPuestosAvanzados;
        for( i = 0; i < numeroPuestosAvanzados; i++) {
        	std::cin >> x[ i ] >> y[ i ];
        }
        for( i = 0; i < numeroPuestosAvanzados; i++ ){
            for( j = i + 1; j < numeroPuestosAvanzados; j++ ){
				distancia = sqrt( ( pow( ( double )x[ i ] - x[ j ], 2 ) + pow( ( double )y[ i ] - y[ j ], 2 ) ) );
                puestosDeAvanzada.push_back( make_pair( distancia, ii( i, j ) ) );
            }        	
		}
        sort( puestosDeAvanzada.begin(), puestosDeAvanzada.end() );
        makeSet( numeroPuestosAvanzados );
        transceptores = 0.0;
        i = 0;
        while( rango > canalesPorSatelite ){
        	std::pair< double, ii > puestoAvanzada = puestosDeAvanzada[ i ];
            unionSet( puestoAvanzada.second.first, puestoAvanzada.second.second, transceptores, puestoAvanzada );
            i++;
		}
        printf( "%.2lf\n", transceptores );
    }
}