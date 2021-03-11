#include <iostream>

using namespace std;

int main(void){
  int arr[9];
  int max = 0;
  int idx = 0;
  for(int i = 0 ; i < 9 ; i++){
    cin >> arr[i];
    if(arr[i] > max){
      max = arr[i];
      idx = i;
    }
  }
  cout << max << endl << idx+1;

}
