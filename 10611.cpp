#include<iostream>

//Juan Esteban Acosta Lopez - Agosto 2021

void binSearchByWembie( int alturasLadyChimps[], int * menor, int * mayor, int numeroLadyChimps, int edadLuchu ){
	int lowMenor = 0, lowMayor = 0;
	int hiMenor = numeroLadyChimps - 1, hiMayor = numeroLadyChimps - 1;
	while( lowMenor <= hiMenor && lowMayor <= hiMayor ){ //una fumaita que en un mismo while se encuentre la mayor y la menor trikzi (ladychimp) para asi tener un mejor uso del tiempo de ejecucion
		int midMenor = ( lowMenor + hiMenor ) / 2, midMayor = ( lowMayor + hiMayor ) / 2;
		if( alturasLadyChimps[ midMenor ] < edadLuchu ){ //si la altura de la trikzi es menor a la edad del bryan xd ps le da (carcel) mentirissssss
			*menor = alturasLadyChimps[ midMenor ]; //como es un puntero llegaria el resultado directamente al menor del main
			lowMenor = midMenor + 1;
		}
		else{
			hiMenor = midMenor - 1; //sino ps se va decrementando el hi
		}
		if( alturasLadyChimps[ midMayor ] > edadLuchu ){ //si la altura de la trikzi es mayor a la edad del bryan xd ps le da pero como ya el legal no hay carcel 8)
			*mayor = alturasLadyChimps[ midMayor ]; //como es un puntero llegaria el resultado directamente al mayor del main
			hiMayor = midMayor - 1;
		}
		else{
			lowMayor = midMayor + 1; //sino ps se va aumentando el low
		}		
	}
}
 
int main(){
    int numeroLadyChimps;
    while( std::cin >> numeroLadyChimps ){ //N
    	int i, edadLuchu, numeroConsultas; //Q
        int alturasLadyChimps[ numeroLadyChimps ]; //arreglo de todas las alturas de las trikzis xd, no me funen
        for( i = 0 ; i < numeroLadyChimps; i++ ){
        	std::cin >> alturasLadyChimps[ i ]; //se van agregando
    	}
    	std::cin >> numeroConsultas;
    	for( i = 0 ; i < numeroConsultas; i++ ){
    		int menor = -1, mayor = -1;
    		std::cin >> edadLuchu; 
    		binSearchByWembie( alturasLadyChimps, &menor, &mayor, numeroLadyChimps, edadLuchu );
    		if( menor == -1 ){
    			std::cout << "X "; //El -1 significa que no hay
			}
			else{
				std::cout << menor << " "; //de lo contrario se mostraria
			}
			if( mayor == -1 ){
    			std::cout << "X" << std::endl; //El -1 significa que no hay
			}
			else{
				std::cout << mayor << std::endl; //de lo contrario se mostraria
			}
    	}
    }
    return 0;   
}
