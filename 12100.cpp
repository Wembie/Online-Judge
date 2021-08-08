#include <iostream>
#include <queue>
#include <algorithm>

const int MAXIMA_CAPACIDAD = 101;

int main(){
	int numeroPrioridades[ MAXIMA_CAPACIDAD ];
    int casos, i, j, numeroTrabajos, posicionTrabajo;
    std::cin >> casos;
    for( i = 0; i < casos; i++ ){
    	std::cin >> numeroTrabajos >> posicionTrabajo;
    	//				  n                  m
    	std::queue< int > indices, prioridades; //en Indices se guardara los indices de 0 a n-1 y en Prioridades ps las prioridades de los trabajos xd
    	for( j = 0; j < numeroTrabajos; j++ ){
    		std::cin >> numeroPrioridades[ j ];
    		prioridades.push( numeroPrioridades[ j ] );
		}
		std::sort( numeroPrioridades, numeroPrioridades + numeroTrabajos ); //Hacemos el sort para que las priodades queden en orden pero del mas bajo al mas alto
		for( j = 0; j < numeroTrabajos; j++ ){
			indices.push( j );
		}
		int tiempo = 0;
		j = numeroTrabajos - 1;
		bool hacer = true;
		while( hacer ){
			if( prioridades.front() == numeroPrioridades[ j ] && indices.front() == posicionTrabajo ){ //si por ejemplo en la cola de prioridades se toma el front y se compara con la ultima posicin de la lista de prioridades
				std::cout << tiempo + 1 << std::endl; // y si son igual y si la cola de indices es igual a la posicion del trabajo que nos dio se imprimiria el tiempo (es decir) Si el elemento frontal de priodades = el elemento más pequeño de la lista ordenada hasta ahora desde el final y indices.front () = posicionTrabajo
				hacer = false; //y se terminaria el ciclo
			}
			else if( prioridades.front() == numeroPrioridades[ j ] ){ //si por ejemplo se toma el front de la cola de prioridades y es igual a la prioridades de la lista en la posicion j se aumenta el tiempo
				tiempo++; //y como no es el indice y la posicion de trabajos iguales se borraria la prioridad y el indice y se bajaraia la prioridad ya que supongamos que nos dan 9 arriba en el if pero como no hay mas 9
				prioridades.pop(); //suponiendo que le sigue otra prioridad al 9 osea 8,7,6,5,4,3,2,1,0 
				indices.pop();
				j--; // y pues se baja la posicion de j para que vaya recorriendo la lista de mayor a menor priodidad osea del final hacia el inicio
			}
			else{
				int temporal = prioridades.front(); //y si por ejemplo no pasa ninguna de estas es q ninguno concuerda con la prioridad correcta ni con la posicion del trabajo que nos daba entonces
				prioridades.pop(); //sacamos los elementos frontales de indices y prioridades y empújelos hasta el final. 
				prioridades.push( temporal );
				temporal = indices.front();
				indices.pop();
				indices.push( temporal ); 
			}	
		}
	}
    return 0;
}
