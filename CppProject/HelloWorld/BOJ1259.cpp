#include <iostream>
#include <string>

using namespace std;

int main(void){
  while(true){
    string S;
    int flag = 0;
    cin >> S;
    if (S == "0") break;
    for (int i = 0; i < S.size() ; i++){
      if(S[i] != S[S.size()-i-1]){
        flag =1 ;
        break;
      }
    }
    if(flag) cout << "no" << endl;
    else cout << "yes" << endl;
  }
}
