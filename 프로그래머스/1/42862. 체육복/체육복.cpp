#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector<int> total(n+2, 0);
    for(auto a:lost){
        total[a]--;
    }
    for(auto a:reserve){
        total[a]++;
    }
    for(int i=1; i<total.size(); i++){
        if(total[i]<0 && total[i-1]>0){
            total[i-1]--;
            total[i]++;
        }
        else if(total[i]<0 && total[i+1]>0){
            total[i+1]--;
            total[i]++;
        }
    }
    for(auto t:total){
        if(t>=0)
            answer++;
    }
    return answer-2;
}