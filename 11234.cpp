#include <iostream>
#include <stack>
#include <queue>
#include <ctype.h>

struct nodo{
	char caracter; //Operadores o Numeros
	nodo * izquierda;
	nodo * derecha;
	nodo( char centro = 0, nodo * izq = 0, nodo * der = 0 ){ //"Constructor del nodo"
		caracter = centro;
		izquierda = izq;
		derecha = der;
	}
};

int main() {
    std::string expresion;
    std::stack< nodo * > pila;
    std::queue< nodo * > cola;
    int vecesARepetir, i, j;
    std::cin >> vecesARepetir;
    for( i = 0; i < vecesARepetir; i++ ){
        std::cin >> expresion;
        std::string expresionFinal;
        for( j = 0; j < expresion.length(); j++ ){	
            if( islower( expresion[ j ] ) ){ //Si encontramos un Numero
            	nodo * arbol = new nodo( expresion [ j ], 0, 0 ); //como encontramos un numero no sabemos que va a tener la izquierda y derecha del arbolito entonces las iniciamos en 0
                pila.push( arbol );
            }
            else{ //Si encontramos un Operador
        		nodo * derecha = pila.top(); //Hijo derecha
                pila.pop();
                nodo * izquierda = pila.top(); // Hijo Izquierda
                pila.pop();
                nodo * padre = new nodo( expresion [ j ], izquierda, derecha ); //Papi
                pila.push( padre );
            }
        }
		cola.push( pila.top() ); //Retornaria (M -> que es de donde se parte todo es decir se divide de la mitad hacia el lado izquierdo y derecho) el patron de patrones en el caso de xyPzwIM quedaria -> xPyMzIw
		while( !cola.empty() ){
			nodo * temporal = cola.front(); //Temporal que coge el front de la cola, Digamos que coge el arbolito M y con ello tiene M->padre,P->izquierdo,I->derecho
			cola.pop(); //Lo borra de la cola para si por ejemplo hay mas mini-arbolitos siga con los demas y no vuelva a coger M
			expresionFinal += temporal->caracter; //Le sumamos (un caracter obviamente) lo q tiene el nodo en la expresion final 
			if( temporal->izquierda ){ //Verifica si en la izquierda no hay un cero y si no hay un 0 es decir hay un arbolito
				cola.push( temporal->izquierda ); //por ejemplo como borramos M en la izquierda del M queda P y dentro de la P en la izquierda quedaria x y en la derecha y
			} // y como en la izquierda de x y y no hay nada es decir un 0 0 y 0 0 hasta ahi llegaria el arbolito
			if( temporal->derecha ){ //Verifica si en la derecha no hay un cero  y si no hay un 0 es decir hay un arbolito
				cola.push( temporal->derecha ); //por ejemplo como borramos M en la derecha del M queda I y dentro de la I en la izquierda quedaria z y en la derecha w
			}// y como en la derecha de z y w no hay nada es decir un 0 0 y 0 0 hasta ahi llegaria el arbolito
		}
		for( j = expresionFinal.length() - 1; j > - 1; j-- ){ //Se imprime en reversa ya en como se extrae directamente de una cola quedaria MPIxyzw
			std::cout << expresionFinal[ j ];	
		}
		std::cout << std::endl;
    }
    return 0;
}
