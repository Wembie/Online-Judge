#include <iostream>

//Juan Esteban Acosta Lopez - Septiembre

const int MAX = 50;
const int MAX_DIRECCIONES = 4;

//Basado en el codigo del profe carlitos con implementaciones para que el programa pueda funcionar acorde a este problema

char tablero[ MAX ][ MAX ];
bool tableroUsado[ MAX ][ MAX ];
int direccionX[ MAX_DIRECCIONES ] = { 0, 1, 0, -1 };
int direccionY[ MAX_DIRECCIONES ] = { 1, 0, -1, 0 };

bool encontroTrampa( int x, int y ){
	int i, nuevaPosicionX, nuevaPosicionY;
	for( i = 0; i < MAX_DIRECCIONES; i++ ){
		nuevaPosicionX = x + direccionX[ i ];
    	nuevaPosicionY = y + direccionY[ i ];
    	if( tablero[ nuevaPosicionX ][ nuevaPosicionY ] == 'T' ){
    		return true;
		}		
	}
	return false;
}

void busquedaProfundidad( int posicionX, int posicionY, int &oro ){
	int i, nuevaPosicionX, nuevaPosicionY;
	if( tablero[ posicionX ][ posicionY ] == '#' || tableroUsado[ posicionX ][ posicionY ] == true ){
		return;
	}
	if( tablero[ posicionX ][ posicionY ] == 'G' ){
		oro++;
	}
	tableroUsado[ posicionX ][ posicionY ] = true;
	if( encontroTrampa( posicionX, posicionY ) ){
		return;
	}
	for( i = 0; i < MAX_DIRECCIONES; i++ ){
		nuevaPosicionX = posicionX + direccionX[ i ];
    	nuevaPosicionY = posicionY + direccionY[ i ];
    	busquedaProfundidad( nuevaPosicionX, nuevaPosicionY, oro );
	}
}

int main() {
	int anchoMapa, alturaMapa, i, j;
	while( scanf( "%d %d", &anchoMapa, &alturaMapa ) == 2 ){ //W / H
		int encontroJugador = 0, oro = 0;
		for( i = 0; i < alturaMapa; i++ ){
			scanf( "%s", tablero[ i ] );
			for( j = 0; j < anchoMapa; j++ ){
				tableroUsado[ i ][ j ] = false;
			}	
		}
		for( i = 0; i < alturaMapa || encontroJugador != 1; i++ ){
            for( j = 0; j < anchoMapa; j++ ){
                if( tablero[ i ][ j ] == 'P' ){
                    busquedaProfundidad( i, j, oro );// dfs
                    encontroJugador = 1;
                }
            }
        }
        std::cout << oro << std::endl;
	}	
	return 0;
}
