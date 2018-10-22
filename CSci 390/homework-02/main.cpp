// 	Name: James Jacob Shaver
// 	ID: 010260091
// 	Email: jjshaver@go.olemiss.edu
// 	Program Source File Name: main.cpp
// 	Last Edit Date: Sunday 02 September 2018
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
#include "helper.h"

using std::cout;
using std::endl;

enum myYear = 4u;

int main(void){

	enum eAcademicYear{Freshmen=1u, Sophmore, Junior, Senior};
	int *pMyYear = &myYear;

	cout << DUMPVAR(myYear) << endl;
	cout << DUMPVAR(pMyYear) << endl;

	*pMyYear = 1u;

	cout << DUMPVAR(myYear) << endl;
}

//myYear = <lvalue>
//Sophmore = <rvalue>
//pMyYear = <lvalue>
//*pMyYear = <rvalue>
