//main.cpp
#include <iostream>
using std::cout;
using std::endl;
#include "complex.h"

int main(void)
{
  // Test real *=
  {
    sComplex<double> C1{1.0, 2.0};
    cout << "Test real *=" << endl;
    cout << "                C1: " << C1 << endl;
    C1 *= 2.0;
    cout << "C1 after C1 *= 2.0: " << C1 << (C1.Re == 2.0 && C1.Im == 4.0 ? ", OK!" : ", ERROR!") <<endl;
  }
  
  // Test real *
  {
    sComplex<double> C1{1.0, 2.0};
    cout << "Test real *" << endl;
    cout << "               C1: " << C1 << endl;
    auto C3 = C1 * 2.0;
    cout << "         C1 * 2.0: " << C3 << (C3.Re == 2.0 && C3.Im == 4.0 ? ", OK!" : ", ERROR!") <<endl;
    cout << "C1 after C1 * 2.0: " << C1 << (C1.Re == 1.0 && C1.Im == 2.0 ? ", OK!" : ", ERROR!") <<endl;
  }
  
  // Test real /=
  {
    sComplex<double> C1{2.0, 4.0};
    cout << "Test real /=" << endl;
    cout << "                C1: " << C1 << endl;
    C1 /= 2.0;
    cout << "C1 after C1 /= 2.0: " << C1 << (C1.Re == 1.0 && C1.Im == 2.0 ? ", OK!" : ", ERROR!") <<endl;
  }
  
  // Test real /
  {
    sComplex<double> C1{2.0, 4.0};
    cout << "Test real /" << endl;
    cout << "             C1: " << C1 << endl;
    auto C3 = C1 / 2.0;
    cout << "        C1 / 2.0: " << C3 << (C3.Re == 1.0 && C3.Im == 2.0 ? ", OK!" : ", ERROR!") <<endl;
    cout << "C1 after C1 / C2: " << C1 << (C1.Re == 2.0 && C1.Im == 4.0 ? ", OK!" : ", ERROR!") <<endl;
  }
  
  // Test complex Inv()
  {
    sComplex<double> C1{2.0, 4.0};
    cout << "Test complex Inv()" << endl;
    cout << "                    C1: " << C1 << endl;
    auto C2 = C1 * C1.Inv();
    auto C3 = C1.Inv();
    cout << "         C1 * C1.Inv(): " << C2 << (C2.Re == 1.0 && C2.Im == 0.0 ? ", OK!" : ", ERROR!") <<endl;
    cout << "C1 after C1 * C1.Inv(): " << C1 << (C1.Re == 2.0 && C1.Im == 4.0 ? ", OK!" : ", ERROR!") <<endl;
  }

  return 0;
}
