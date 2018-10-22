#include <iostream>
#include <ostream>
using std::ostream;
using std::cout;
using std::endl;

typedef double T;

class sComplex{
public:
	sComplex(void) : Re(0.0), Im(0.0) {return;}
	sComplex(T Ree, T Imm) : Re(Ree), Im(Imm) {return;}
	sComplex(const sComplex &p) : Re(p.Re), Im(p.Im){return;}
	~sComplex(void){return;}
	inline sComplex operator+ (const sComplex &rhs) const {return sComplex{Re + rhs.Re, Im + rhs.Im};}
	inline sComplex &operator+=(const sComplex &rhs){Re+=rhs.Re; Im+=rhs.Im; return *this;}
	inline sComplex operator- (const sComplex &rhs) const {return sComplex{Re - rhs.Re, Im - rhs.Im};}
	inline sComplex &operator-=(const sComplex &rhs){Re-=rhs.Re; Im-=rhs.Im; return *this;}
	T Re, Im;
};


ostream &operator<<(ostream &s, const sComplex  &p){
	s << "(" << p.Re << ", " << p.Im << "j)"; return s;}
