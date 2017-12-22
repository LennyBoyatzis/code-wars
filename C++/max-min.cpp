// The two lines below are directives - interpreted by the preprocessor
// They are instructing the preprocessor to include a section of standard c++ code
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int min(vector<int> list) {
  return *(min_element(list.begin(), list.end()));
}

int max(vector<int> list) {
  return *(max_element(list.begin(), list.end()));
}

int main() {
  cout << "Hello world!";
  int foo[5] = { 16, 2, 77, 40, 12071 };
  /* int bar[5] = { 10, 20, 30 }; */
}
