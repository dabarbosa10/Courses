#include <iostream>
#include <cmath>

int get_change(int m) {
	int n;
   n=floor(m/10)+floor((m%10)/5)+(m%5);
	return n;
}

int main() {
  int m;
  std::cin >> m;
  std::cout << get_change(m) << '\n';
}
