// 	Name: James Jacob Shaver
// 	ID: 010260091
// 	Email: jjshaver@go.olemiss.edu
// 	Program Source File Name: main.cpp
// 	Last Edit Date: Saturday 22 October 2018
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
#include <string>
#include <algorithm>

using namespace std;

int main(void)
{
	string s{"Hello world!"};
	cout << "s before transform: " << s << endl;
	transform(s.begin(), s.end(), s.begin(), ::toupper);
	cout << "s after transform: " << s << endl;

	return 0;

}
