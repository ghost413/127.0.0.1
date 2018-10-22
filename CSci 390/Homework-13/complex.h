#include <iostream>
#include <ostream>
using namespace std;

template<typename T>
struct sComplex{
	sComplex(void) : Re(0.0), Im(0.0) {return;}
	sComplex(const T Ree) : Re(Ree), Im (T(0.0)){return;}
	sComplex(T Ree, T Imm) : Re(Ree), Im(Imm) {return;}
	sComplex(const sComplex &Obj) : Re(Obj.Re), Im(Obj.Im){return;}
	~sComplex(void){return;}
	inline sComplex operator+ (const T Ree) const {return sComplex{this -> Re + Ree, this -> Im};}
	inline sComplex &operator+=(const T Ree){this -> Re+=Ree, this -> Im; return *this;}
	inline sComplex operator- (const T Ree) const {return sComplex{this -> Re - Ree, this -> Im};}
	inline sComplex &operator-=(const T Ree){this -> Re-=Ree, this -> Im; return *this;}
	inline sComplex Conj(void) const {return sComplex{Re, -Im};}
	T Re, Im;
	
};

template<typename T>
ostream &operator<<(ostream &s, const sComplex<T>  &p){
	s <<  "(" << p.Re << (p.Im >= T(0.0) ? "+" : "") <<  p.Im << "j)";return s;}
