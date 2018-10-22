// 	Name: James Jacob Shaver
// 	ID: 010260091
// 	Email: jjshaver@go.olemiss.edu
// 	Program Source File Name: newton.h
// 	Last Edit Date: Saturday 30 September 2018
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
#include <ostream>

using std::ostream;
using std::cout;
using std::endl;

struct thing{
	thing(void) : skuNumber(0), unitCost(0.0) {return;}
	thing(int _skuNumber, double _unitCost) : 
	skuNumber(_skuNumber), unitCost(_unitCost) {return;}
	virtual ~thing(void){
		cout << "~thing(void)\n";
		return; 
	}
	int skuNumber;
	double unitCost;	
};
ostream &operator << (ostream &File, const thing &nThing){
	File << nThing.skuNumber << ", " << nThing.unitCost;
	return File;
}
