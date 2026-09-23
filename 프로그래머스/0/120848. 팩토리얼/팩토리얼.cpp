#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int temp = 1;
    int i=1;
    while (temp <= n){
        i++;        
        temp*=i;
    }
    
    // for(int i=1; i<11; i++){
    //     if
    // }
    return i-1;
}