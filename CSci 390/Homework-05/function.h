#include <iostream>
#include "helper.h"
#include <math.h>

template<typename T> 
T hypotenuse(T x, T y);

template<typename T> 
T hypotenuse(T x, T y){
	return double(sqrt(pow(x, 2) + pow(y, 2)));
}