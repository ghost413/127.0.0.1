//main.cpp
#include <iostream>
using std::cout;
using std::endl;
#include "complex.h"

int main(void)
{
  // Test real constructor
  {
    sComplex<double> C1{1.0};
    cout << "Test real constructor: sComplex<double> C1{1.0}" << endl;
    cout << "C1: " << C1 << (C1.Re == 1.0 && C1.Im == 0.0 ? ", OK!" : ", ERROR!") <<endl;
  }
  
  // Test real +=
  {
    sComplex<double> C1{1.0, 1.0};
    cout << "Test real +=" << endl;
    cout << "C1: " << C1 << endl;
    C1 += 2.0;
    cout << "C1 after C1 += 2.0: " << C1 << (C1.Re == 3.0 && C1.Im == 1.0 ? ", OK!" : ", ERROR!") <<endl;
  }

  // Test real -=
  {
    sComplex<double> C1{1.0, 1.0};
    cout << "Test real -=" << endl;
    cout << "C1: " << C1 << endl;
    C1 -= 2.0;
    cout << "C1 after C1 -= 2.0: " << C1 << (C1.Re == -1.0 && C1.Im == 1.0 ? ", OK!" : ", ERROR!") <<endl;
  }

  // Test real +
  {
    sComplex<double> C1{1.0, 1.0};
    cout << "Test real +" << endl;
    cout << "C1: " << C1 << endl;
    auto C2 = C1 + 2.0;
    cout << "C1 after C1 + 2.0: " << C1 << (C1.Re == 1.0 && C1.Im == 1.0 ? ", OK!" : ", ERROR!") <<endl;
    cout << "         C1 + 2.0: " << C2 << (C2.Re == 3.0 && C2.Im == 1.0 ? ", OK!" : ", ERROR!") <<endl;
  }

  // Test real -
  {
    sComplex<double> C1{1.0, 1.0};
    cout << "Test real -" << endl;
    cout << "C1: " << C1 << endl;
    auto C2 = C1 - 2.0;
    cout << "C1 after C1 - 2.0: " << C1 << (C1.Re == 1.0 && C1.Im == 1.0 ? ", OK!" : ", ERROR!") <<endl;
    cout << "         C1 - 2.0: " << C2 << (C2.Re == -1.0 && C2.Im == 1.0 ? ", OK!" : ", ERROR!") <<endl;
  }

  // Test Conj()
  {
    sComplex<double> C1{1.0, 1.0};
    cout << "Test Conj()" << endl;
    auto C2 = C1.Conj();
    cout << "C1 after C1.Conj(): " << C1 << (C1.Re == 1.0 && C1.Im == 1.0 ? ", OK!" : ", ERROR!") <<endl;
    cout << "         C1.Conj(): " << C2 << (C2.Re == 1.0 && C2.Im == -1.0 ? ", OK!" : ", ERROR!") <<endl;
  }

  return 0;
}
