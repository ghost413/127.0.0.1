
#include <ostream>

template<typename T>
struct sComplex{

	sComplex(void) : Re(T(0.0)), Im(T(0.0)) {return;}
	sComplex(const T Ree) : Re(Ree), Im(T(0.0)) {return;}
	sComplex(const T Ree, const T Imm) : Re(Ree), Im(Imm) {return;}
	sComplex(const sComplex &Obj) : Re(Obj.Re), Im(Obj.Im) {return;}
	virtual ~sComplex(void) {return;}
	  
	inline sComplex &operator+=(const sComplex &rhs) {Re += rhs.Re; Im += rhs.Im; return *this;}
	inline sComplex &operator-=(const sComplex &rhs) {Re -= rhs.Re; Im -= rhs.Im; return *this;}
	inline sComplex &operator*=(const sComplex &rhs) {T Re1 = Re*rhs.Re - Im*rhs.Im; Im = Re*rhs.Im + Im*rhs.Re; Re = Re1; return *this;}
	inline sComplex operator+(const sComplex &rhs) const {return sComplex{Re + rhs.Re, Im + rhs.Im};}
	inline sComplex operator-(const sComplex &rhs) const {return sComplex{Re - rhs.Re, Im - rhs.Im};}
	inline sComplex operator*(const sComplex &rhs) const {return sComplex{Re * rhs.Re - Im * rhs.Im, Re * rhs.Im + rhs.Re * Im};}
	  
	inline sComplex &operator+=(const T &rhs) {Re += rhs; return *this;}
	inline sComplex &operator-=(const T &rhs) {Re -= rhs; return *this;}
	inline sComplex &operator*=(const T &rhs) {Re *= rhs; return *this;}
	inline sComplex operator+(const T &rhs) const {return sComplex{Re + rhs, Im};}
	inline sComplex operator-(const T &rhs) const {return sComplex{Re - rhs, Im};}
	inline sComplex operator*(const T &rhs) const {return sComplex{Re * rhs, Im};}
	  
	inline sComplex Conj(void) const {return sComplex{Re, -Im};}
	inline T Conjugate(void) const {return T{Re * Re + Im * Im};}

	T Re, Im;
};

template<typename T>
std::ostream &operator << (std::ostream &s, const sComplex<T> &p){
	s <<  "(" << p.Re << (p.Im >= T(0.0) ? "+" : "") <<  p.Im << "j)";
	return s;
}