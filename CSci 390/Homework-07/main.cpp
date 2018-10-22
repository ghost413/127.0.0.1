#include <iostream>
#include <cmath>

using std::cout;
using std::endl;

int main(void)
{
	auto doWhile = 0;
	auto forLoop = 0;
	auto whileLoop = 0;
	auto gauss = 0;
	auto num = 0;

	gauss = (10 * 9)/2;

	cout << "Gauss' Formula: " << gauss << endl;

	do{
		doWhile += num;
		num++;
	}
	while(num < 10);

	cout << "Do-While Loop: " << doWhile << endl;

	for(int i = 0; i < 10; i++){
		forLoop += i;
	}

	cout << "For-Loop: " << forLoop << endl;

	num = 0;
	while(num < 10){
		whileLoop += num;
		num ++;
	}

	cout << "While-Loop: " << whileLoop << endl;

	std::cin.get();
	return 0;
}