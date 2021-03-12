#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main(void) {
  int T;
  string S;

  cin >> T ;
  
  for(int i = 0; i < T; i++){
    stack<char> stack;
    cin >> S;
    int Flag = 0;
    for(int j = 0 ; j<S.size(); j++){
      if(S[j] == '('){
        stack.push(S[j]);

      }
      else{
        if(stack.empty()){
          Flag = 1;
          break;
        }
        stack.pop();
      }
    }
    if (Flag == 1 ) cout << "no" << endl;
    else{
      if(stack.empty()){
        cout << "yes" << endl;
      }
      else cout << "no" << endl;
    }
  }
}