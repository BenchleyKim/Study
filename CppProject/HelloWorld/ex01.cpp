#include <iostream>
#include <string>
using namespace std;

int main(void){  
  int t;
  std::cin >> t;
  for(int i = 0 ; i < t; i++){
    int r;
    string S;
    cin >> r >> S ;
    for(int j = 0; j < S.length(); j++)
      for(int k =0 ; k < r ; k++)
        cout << S[j];
    cout<< endl;
  }
  return 0;
}