#include <string>
#include <vector>

using namespace std;

int solution(vector<int> sides) {
    int answer = 0;
    int a1, a2;
    //가장 긴변
    if(sides[0]>sides[1]) {
        a1=sides[1];
        a2=sides[0];
        }
    else{
        a1=sides[0];
        a2=sides[1];
    }
    for(int i = a2; i<a1+a2; i++){
        answer++;
    }
    //가장 긴변은 아님
    for (int i=a2-a1+1; i<a2;i++ ){
        answer++;
    } 
    
    return answer;
}