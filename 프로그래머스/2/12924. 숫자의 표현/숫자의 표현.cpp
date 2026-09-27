#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(int n) {
    int answer = 1;
    for(int i=1; i<n/2+1; i++){
        int sum=0;
        int j=i;
        while(sum<=n){
            if(sum==n) {
                answer++;
                break;
            }
            sum+=(j);
            j++;
        }
    }
    return answer;
}