//object.h:
#include <cstdint>
#include <cstdlib>

struct sArray
{
	if (n >= 0){
	sArray(void) { return; }
	sArray(const uint32_t n) { Array = (double *)
		malloc(n * sizeof(double)); return; }
	}
	else throw "ERROR!: This didn't work like you thought it would!";
	virtual ~sArray(void) { free(Array); return; }
	double &operator[] (const uint32_t i)
	{ return Array[i]; }
	sArray(void) = delete;

double *Array;
};