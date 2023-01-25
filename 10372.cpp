#include <iostream>	
#include <math.h>

//Juan Esteban Acosta Lopez - Septiembre 2021

/*Formulas
Velocidad inicial = raiz( ( alcance MAX horizontal * gravedad  ) / ( seno 2 ( angulo ) ) )
Velocidad en x = Velocidad inicial * coseno( angulo )
Velocidad en y = Velocidad inicial * seno( angulo )
*/

int main(){
	int n;
	while( std::cin >> n ){
		double alturaEdificios[ n ];
		double distanciaSuperMan[ n ];
		double low, hi, mid, alcanceMaxHorizontal = 0, angulo, velocidadInicial;
		const float gravedad = 9.8;
		int i;
		for( i = 0 ; i < n; i++ ){
			std::cin >> alturaEdificios[ i ] >> distanciaSuperMan[ i ];
			alcanceMaxHorizontal += distanciaSuperMan[ i ]; //se hace la sumatoria de todas las distancias para saber el alcance maximo
		}
		low = 0;
		hi = acos( -1 ) / 2;
		while( hi - low > 0.01 ){ //hasta que sea mayor al eps q seria 0.01
			mid = ( low + hi ) / 2;
			angulo = mid; //tomamos que el angulo va hacer nuestro mid para poder ir probando
			velocidadInicial = sqrt( ( alcanceMaxHorizontal * gravedad ) / sin( 2 * angulo ) ); //de acuerdo a la formula se encuentra dicha velocidad inicial
			double tiempo, alcance, altura;
			double velocidadEnX = velocidadInicial * cos( angulo ); //de acuerdo a la formula se encuentra dicha velocidad en x
			double velocidadEnY = velocidadInicial * sin( angulo ); //de acuerdo a la formula se encuentra dicha velocidad en y
			/*
			Se que tengo q recorrer la lista hasta n y con ello ir encontrado el tiempo y el alcance de cada uno de los edificios
			y con ello ir aplicando las formulas de velocidad en x, y al igual que ir comparando el mid si puede pasar a una minima altura del eficio para todos los casos y si no sirve ir cambiando el mid
			dependiendo si es menor o mayor y con ello ir controlando el low y el hi para dar con el angulo y la velocidad correcta
			for( i = 0 ; i < n; i++ ){
				pero no me alcanzo el tiempo :c
			}
			if( altura < alturaEdificios[ i ] ){
				low = mid;
			}
			else{
				hi = mid;
			}
			Es practicamente lo mismo que hago en wifi sino que aplicando las formulas
			*/
		}
		//angulo / velocidad inicial
		printf( "%.2f %.2f", angulo, velocidadInicial );
	}
	return 0;
}
