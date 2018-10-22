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
#include "newton.h"
#include <cmath>

using std::cout;
using std::endl;

int main(void){

	auto tolerance = 1.0e-20L;
	auto guess = 1.0L;
	auto f = [](const long double x){return (x * x) - 2.0L;};
	auto df = [](const long double x){return 2.0L * x;};

	auto n = Newton<long double>(guess, tolerance, f, df);
	n;

	std::cin.get();

	return 0;
}

