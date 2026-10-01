#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector<int> total(n+1, 0);
    for(auto a:lost){
        total[a]--;
    }
    for(auto a:reserve){
        total[a]++;
    }
    for(int i=1; i<n+1; i++){
        if(total[i]<0){
            if(total[i-1]>0 &&i>=2){
                total[i-1]--;
                total[i]++;
            }
            else if(total[i+1]>0&&i<n){
                total[i+1]--;
                total[i]++;
            }
        }
    }
    for(auto t:total){
        if(t>=0)
            answer++;
    }
    return answer-1;
}