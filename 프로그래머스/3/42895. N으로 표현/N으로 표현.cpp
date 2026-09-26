#include <string>
#include <vector>
#include <set>
using namespace std;
int solution(int N, int number) {
    int answer = 0;
    int repeat = 0;
    vector<set<int>> dp(9);
    
    for(int i=1; i<=8; i++){
        repeat = repeat*10 +N;
        dp[i].insert(repeat);
    }
    for(int i=1; i<9; i++){
        for(int j=1; j<i; j++){
            for(auto a1: dp[j]){
                for(auto b1: dp[i-j]){
                    dp[i].insert(a1+b1);
                    if(a1>b1)   dp[i].insert(a1-b1);
                    else    dp[i].insert(-a1+b1);
                    dp[i].insert(a1*b1);
                    if(b1!=0) dp[i].insert(a1/b1);
                }
            }
        }
        if(dp[i].find(number)!=dp[i].end()) return i;
    }
    
    return -1;
}