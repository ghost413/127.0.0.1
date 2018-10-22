//main.cpp:
#include <iostream>
#include "object.h"

using std::cout;
using std::endl;

int main(int argc, char *argv[]){

	try{
	sArray array(11u);
	array[1u] = 29u;
	cout << "Array [1u]: " << array[1u] << endl;
	}
	catch (const char *e){
		std::cout << "Error: " << e << std::endl;
	}
return 0;
}
