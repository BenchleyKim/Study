#include <iostream>

using namespace std;
int main(void){
  int n , r ;
  cin >> n >> r;
  int ans = 1;
  int k = r;
  for(int i = 0 ; i < r ; i ++ ){
    ans *= n;
    ans /= i+1;
    n--;
  }
  cout << ans;

}