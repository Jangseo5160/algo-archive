#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int temp = 1;
    int i=1;
    // while (temp <= n){
    //     temp*=i;
    //     i++;        
    // }
    
    for(int i =1; i<11; i++){
        temp*=i;
        if(temp>n){
            return i-1;
        }
    }
}