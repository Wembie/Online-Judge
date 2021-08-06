#include <iostream>
#include <stack>
#include <string>

const int CHAR_TO_STRING = 1;

int main(){
    std::string expresion;
    while( getline( std::cin, expresion ) ){
        std::stack< std::string > pila;
        int i, posicionError = 0;
        for( i = 0; i < expresion.length(); i++ ){
            posicionError++;
            if( expresion[ i ] == '(' || expresion[ i ] == '{' || expresion[ i ] == '[' || expresion[ i ] == '<' ){
                if( expresion[ i ] == '(' && expresion[ i + 1 ] == '*'){
                    pila.push( "(*" );
                    i++;
                }
                else{
                    std::string caracter( CHAR_TO_STRING, expresion[ i ] ); //Convertidor de Char a String
                    pila.push( caracter );
                }
            }
            else if( ( expresion[ i ] == ')' || expresion[ i ] == '}' || expresion[ i ] == ']' || expresion[ i ] == '>' ) || ( expresion[ i ] == '*' && expresion[ i + 1 ] == ')' ) ){
                if( pila.empty() ){
                    break;
                }
                if( expresion[ i ] == ')'){
                	if( pila.top() != "(" ){
                        break;
                    }
                    pila.pop();
				}
				else if( expresion[ i ] == '}' ){
					if( pila.top() != "{" ){
                        break;
                    }
                    pila.pop();	
				} 
				else if( expresion[ i ] == ']' ){
					if( pila.top() != "[" ){
                        break;
                    }
                    pila.pop();	
				}
				else if( expresion[ i ] == '>' ){
					if( pila.top() != "<" ){
                        break;
                    }
                    pila.pop();
				}
				else if( expresion[ i ] == '*' && expresion[ i + 1 ] == ')' ){
					if( pila.top() != "(*" ){
                        break;
                    }
                    i++;
                    pila.pop();
				}
            }
        }
        if( i < expresion.length() || !pila.empty() ){
        	if( i >= expresion.length() && !pila.empty() ){
        		posicionError++;
			}
    		std::cout << "NO " << posicionError;
        }
    	else{
    	    std::cout << "YES";
    	}
    	std::cout << std::endl;
    }
    return 0;
}