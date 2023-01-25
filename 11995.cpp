#include <iostream>
#include <stack>
#include <queue>	

//Juan Esteban Acosta Lopez - Septiembre 2021

int main(){
	int n;
	while( std::cin >> n ){
		std::stack< int > stack; //Pila
        std::queue< int > queue; //Cola
        std::priority_queue< int > priorityQueue; //Cola de Prioridad
        bool sePuedeConStack = true, sePuedeConQueue = true, sePuedeConPriorityQueue = true; //iniciamos las variables con las q se pueden usar las estrucutras de una vez en true para ahorrar lineas
        int comando, x, i;
        for( i = 0 ; i < n; i++ ){
        	std::cin >> comando >> x;
        	if( comando == 1 ){ //Si el comando es 1 se agrega con cada estructura
        		stack.push( x );
        		queue.push( x );
        		priorityQueue.push( x );
			}
			else{ //Si el comando es diferente de 1 se verifica con cada estructura
				if( !stack.empty() && stack.top() == x ){ //Se verifica que la pila no este vacia y miramos si el top es igual al numero x que nos dan
					stack.pop(); //Si da verdadero se elimina (el top) de dicha pila
				}
				else{
					sePuedeConStack = false; //Si no ps se asigna como falso
				}
				if( !queue.empty() && queue.front() == x ){ //Se verifica que la cola no este vacia y miramos si el front es igual al numero x que nos dan
					queue.pop(); //Si da verdadero se elimina (el front) de dicha cola
				}
				else{
					sePuedeConQueue = false; //Si no ps se asigna como falso
				}
				if( !priorityQueue.empty() && priorityQueue.top() == x ){ //Se verifica que la cola de prioridad no este vacia y miramos si el top es igual al numero x que nos dan
					priorityQueue.pop(); //Si da verdadero se elimina (el top) de dicha cola de prioridad
				}
				else{
					sePuedeConPriorityQueue = false; //Si no ps se asigna como falso
				}
			}
    	}
    	if( sePuedeConStack == true && sePuedeConQueue == false && sePuedeConPriorityQueue == false ){
    		std::cout << "stack" << std::endl;
		}
		else if( sePuedeConStack == false && sePuedeConQueue == true && sePuedeConPriorityQueue == false ){
    		std::cout << "queue" << std::endl;
		}
		else if( sePuedeConStack == false && sePuedeConQueue == false && sePuedeConPriorityQueue == true ){
    		std::cout << "priority queue" << std::endl;
		}
		else if( sePuedeConStack == false && sePuedeConQueue == false && sePuedeConPriorityQueue == false ){
    		std::cout << "impossible" << std::endl;
		}
		else{
			std::cout << "not sure" << std::endl;
		}
	}
	return 0;
}
