#if defined(Msg)
#include "Function.h"
#include <iostream>
#endif

#if defined void  Msg(const char *&Message) {
	std::cout << Message << std::endl;
	return ;
}

#endif