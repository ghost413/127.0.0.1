
#include <iostream>
using std::cout;
using std::endl;
#include "complex.h"

int main(void)
{
	// Test Conjugate
	{
		sComplex<double> C1{1.0, 2.0};
		cout << "Test Conjugate" << endl;
		auto C2 = C1.Conjugate();
		cout << "         C1.Conjugate(): " << C2 << (C2 == 5.0 ? ", OK!" : ", ERROR!") <<endl;
		cout << "C1 After C1.Conjugate(): " << C1 << (C1.Re == 1.0 && C1.Im == 2.0 ? ", OK!" : ", ERROR!") <<endl;
	}
	
	// Test complex *=
	{
		sComplex<double> C1{1.0, 2.0};
		sComplex<double> C2{3.0, 4.0};
		cout << "Test complex *=" << endl;
		cout << "C1: " << C1 << endl;
		cout << "C2: " << C2 << endl;
		C1 *= C2;
		cout << "C1 after C1 *= C2: " << C1 << (C1.Re == -5.0 && C1.Im == 10.0 ? ", OK!" : ", ERROR!") <<endl;
		cout << "C2 after C1 += C2: " << C2 << (C2.Re == 3.0 && C2.Im == 4.0 ? ", OK!" : ", ERROR!") <<endl;
	}
	
	// Test complex *
	{
		sComplex<double> C1{1.0, 2.0};
		sComplex<double> C2{3.0, 4.0};
		cout << "Test complex *" << endl;
		cout << "C1: " << C1 << endl;
		cout << "C2: " << C2 << endl;
		auto C3 = C1 * C2;
		cout << "C1 * C2: " << C3 << (C3.Re == -5.0 && C3.Im == 10.0 ? ", OK!" : ", ERROR!") <<endl;
		cout << "C1 after C1 * C2: " << C1 << (C1.Re == 1.0 && C1.Im == 2.0 ? ", OK!" : ", ERROR!") <<endl;
		cout << "C2 after C1 * C2: " << C2 << (C2.Re == 3.0 && C2.Im == 4.0 ? ", OK!" : ", ERROR!") <<endl;
	}

	return 0;
}
