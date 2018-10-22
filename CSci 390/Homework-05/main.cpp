//main.cpp:
#include <iostream>
#include "function.h"
#include "helper.h"

int main(void)
{
  auto RV1 = hypotenuse<>(3.0f, 4.0f);
  std::cout << "hypotenuse<>(3.0f, 4.0f): " << RV1 << std::endl;
  std::cout << DUMPVAL(RV1) << std::endl;

  auto RV2 = hypotenuse<>(1.0, 1.0);
  std::cout << "hypotenuse<>(1.0, 1.0): " << RV2 << std::endl;
  std::cout << DUMPVAL(RV2) << std::endl;
  
  std::cin.get();
  return 0;
}
