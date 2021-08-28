#include<iostream>

//Juan Esteban Acosta Lopez - Agosto

void binSearchByWembie( int alturasLadyChimps[], int * menor, int * mayor, int numeroLadyChimps, int edadLuchu ){
	int lowMenor = 0, lowMayor = 0;
	int hiMenor = numeroLadyChimps - 1, hiMayor = numeroLadyChimps - 1;
	while( lowMenor <= hiMenor && lowMayor <= hiMayor ){
		int midMenor = ( lowMenor + hiMenor ) / 2, midMayor = ( lowMayor + hiMayor ) / 2;
		if( alturasLadyChimps[ midMenor ] < edadLuchu ){
			*menor = alturasLadyChimps[ midMenor ];
			lowMenor = midMenor + 1;
		}
		else{
			hiMenor = midMenor - 1;
		}
		if( alturasLadyChimps[ midMayor ] > edadLuchu ){
			*mayor = alturasLadyChimps[ midMayor ];
			hiMayor = midMayor - 1;
		}
		else{
			lowMayor = midMayor + 1;
		}		
	}
}
 
int main(){
    int numeroLadyChimps;
    while( std::cin >> numeroLadyChimps ){ //N
    	int i, edadLuchu, numeroConsultas; //Q
        int alturasLadyChimps[ numeroLadyChimps ];
        for( i = 0 ; i < numeroLadyChimps; i++ ){
        	std::cin >> alturasLadyChimps[ i ]; 
    	}
    	std::cin >> numeroConsultas;
    	for( i = 0 ; i < numeroConsultas; i++ ){
    		int menor = -1, mayor = -1;
    		std::cin >> edadLuchu; 
    		binSearchByWembie( alturasLadyChimps, &menor, &mayor, numeroLadyChimps, edadLuchu );
    		if( menor == -1 ){
    			std::cout << "X ";
			}
			else{
				std::cout << menor << " ";
			}
			if( mayor == -1 ){
    			std::cout << "X" << std::endl;
			}
			else{
				std::cout << mayor << std::endl;
			}
    	}
    }
    return 0;   
}
