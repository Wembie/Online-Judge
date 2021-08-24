#include<iostream>
 
int main(){
    int years, numeroPopes ,i;
    while( std::cin >> years ){
        std::cin >> numeroPopes;
        int popes[ numeroPopes ]; //Lista de popes
        int maximo = 0, j = 0, k = 0, primero, ultimo;
        for( i = 0 ; i < numeroPopes; i++ ){
        	std::cin >> popes[ i ]; //Agregacion de los popes la lista
        	if( i == 0 ){ //Si i = 0 entonces tomamos como si fuera el primer maximo y el ultimo maximo como dicho numero para poder evaluarlo luego
        		primero = popes[ i ]; //First
        		ultimo = popes[ i ]; //Last
			}
		}    
		//Tomamos a k como si fueran los indices de primer elemento hacia el ultimo y Tomamos a j como si fueran los indices del ultimo elemento hacia el primero
        while( j < numeroPopes - 1 ){ //recorremos la lista de popes hasta -1 ya que las listan terminan hasta len(lista)-1 :D
            j++;
            while( popes[ j ] - popes[ k ] >= years ){ //Verificacion de si el elemento que hay en popes[ j ] - el de popes [ k ] son mayores o iguales ( >= ) al year inicial que en este ejemplo seria 5
            	//Por ejemplo en el caso cuando entra a este igual del example es que popes[ j ] = 6y con j = 3 y popes [ k ] = 1 y con k = 0, entonces 6 - 1 = 5 el cual da con el year inicial y asiiii.......
                k++; //y ps se va aumentando la k :v
            }
            if( j - k + 1 > maximo ){ //j y k ( indices ) -> tomando el input del example mira si j - k q seria la diferencia para dividir la lista por ejemplo la primera vez seria, j = 1 y k = 0, entonces 1 - 0 = 1, + 1 = 2 entonces 2 es mayor ( > ) al maximo el cual seria 0
                maximo = j - k + 1; //Colocamos el nuevo maximo a su valor
                primero = popes[ k ]; //Por linea 16
                ultimo = popes[ j ]; //x2
            }       
        }
        std::cout << maximo << " " << primero << " " << ultimo << std::endl;
    }
    return 0;   
}
