#include <iostream>
#include "complex.h"
#include "helper.h"

using std::cout;
using std::endl;

int main(int argc, char const *argv[])
{
	sComplex v1{10.0, 9.0};

	cout << "v1 of sComplex: " << v1 << endl;

	sComplex Origin;
	sComplex point{1.0, 1.0};
	Origin += point;
	cout << DUMPOBJ(Origin) << endl;
	Origin + point;
	cout << DUMPOBJ(Origin) << endl;
	Origin -= point;
	cout << DUMPOBJ(Origin) << endl;
	Origin - point;
	cout << DUMPOBJ(Origin) << endl;

	return 0;
}
