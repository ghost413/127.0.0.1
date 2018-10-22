// 	Name: James Jacob Shaver
// 	ID: 010260091
// 	Email: jjshaver@go.olemiss.edu
// 	Program Source File Name: newton.h
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

#include <iomanip>
#include <iostream>
#include <cmath>

using std::cout;
using std::endl;
using std::abs;
using std::setprecision;

template<typename T> 
T Newton(T guess, T Tol, T (*f)(const T x), T (*df)(const T x));

template<typename T> 
T Newton(T guess, T Tol, T (*f)(const T x), T (*df)(const T x)){
	T xn;
	T xnN = guess;
	T tn;
	T difference;
	T tolerance = Tol;
	T counter = 1;
	T thing = (xn - xnN);
	do{
		xn = xnN;
		xnN = xn - f(xn)/df(xn);
		difference = xn - xnN;
		guess = xnN;
		difference = abs(difference);
		cout << "Iteration " << counter << ", xn: " << setprecision(32) 
		<< guess << endl;
		counter++;
	}
	while(counter > 7);
}

