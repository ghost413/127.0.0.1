// 	Name: James Jacob Shaver
// 	ID: 010260091
// 	Email: jjshaver@go.olemiss.edu
// 	Program Source File Name: main.cpp
// 	Last Edit Date: Saturday 22 September 2018
// 	Course Information: CSci 390
// 	Program Description:
// 	Sources Consulted:
// 	Honor Code Statement: In keeping with the honor code policies of the
// 	University of Mississippi, the School of Engineering, and the Department of
// 	Computer and Information Science, I affirm that I have neither given nor
// 	received assistance on this programming assignment. This assignment
// 	represents my individual, original effort.
// 		...My Signature is on File.

// 			'Was wir für uns selbst tun, stirbt mit uns.
// 	Was wir für andere und die Welt tun, bleibt und ist unsterblich.'

#include <iostream>
#include "absval.h"
#include "helper.h"

using std::cin;
using std::cout;
using std::endl;

int main(void){
	int intValue = absval<>(-3);
	cout << "absval<>(-3): " << intValue << endl;
	cout << DUMPVAL(intValue) << endl;

	unsigned int uIntValue = absval<>(-3);
	cout << "absval<>(-3): " << uIntValue << endl;
	cout << DUMPVAL(uIntValue) << endl;

	double doubleValue = absval<>(-3.14159);
	cout << "\nabsval<>(-3.14159): " << doubleValue << endl;
	cout << DUMPVAL(doubleValue) << endl;

	long longValue = absval<>(-30000);
	cout << "\nabsval<>(-3000): " << longValue << endl;
	cout << DUMPVAL(longValue) << endl;

	std::cin.get();
	return 0; 
}