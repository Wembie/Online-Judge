#include <iostream>

//Juan Esteban Acosta Lopez - Octubre

const int MAX = 10001;

int encontro[ MAX ];
int debe[ MAX ];
int dinero[ MAX ];

int encontrar( int amigo ){
	if( encontro[ amigo ] == amigo ){
		return amigo;
	}
	else{
		return encontro[ amigo ] = encontrar( encontro[ amigo ] );
	}
}

int main(){
	int i, j, totalPruebas, amigos, amistadesRestantes, amigoX, amigoY;
	bool posible;
	std::cin >> totalPruebas;
	for( i = 0; i < totalPruebas; i++ ){
		posible = true;
		std::cin >> amigos >> amistadesRestantes;
		for( j = 0; j < amigos; j++ ){
			std::cin >> debe[ j ];
			encontro[ j ] = j;
			dinero[ j ] = 0;
		}
		for( j = 0; j < amistadesRestantes; j++ ){
			std::cin >> amigoX >> amigoY;
			encontro[ encontrar( amigoX ) ] = encontrar( amigoY );		
		}
		for( j = 0; j < amigos; j++ ){
			dinero[ encontrar( j ) ] += debe[ j ];
		}
		j = 0;
		while( j < amigos && posible ){
			if( dinero[ j ] != 0 ){
				posible = false;
				j = amigos;
			}
			j++;
		}
		if( posible ){
			std::cout << "POSSIBLE" << std::endl;
		}	
		else{
			std::cout << "IMPOSSIBLE" << std::endl;
		}				
	}	
	return 0;
}
