#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector<int> total(n+1, 1);
    for(auto a:lost){
        total[a]--;
    }
    for(auto a:reserve){
        total[a]++;
    }
    for(int i=1; i<n+1; i++){
        if(total[i]==0){
            if(total[i-1]==2 && i>=2){
                total[i-1]--;
                total[i]++;
            }
            else if(total[i+1]==2 && i<=n-1){
                total[i+1]--;
                total[i]++;
            }
        }
    }
    for(auto i:total){
        if(i>=1){
            answer++;
        }
    }
    return answer-1;
}