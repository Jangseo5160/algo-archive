#include <string>
#include <vector>
#include<set>

using namespace std;

int solution(int N, int number) {
    int answer = 0;
    vector<set<int>> dp(9);
    int temp=0;
    for(int i=1; i<9; i++){
        temp=temp*10+N; //5, 55, 555, 55555555
        dp[i].insert(temp);
    }
    for(int i=1; i<9; i++){
        for(int j=1; j<9; j++){
            if(i+j<9){
                for(auto num1:dp[i]){
                    for(auto num2:dp[j]){
                        dp[i+j].insert(num1+num2);
                        dp[i+j].insert(num1*num2);
                        dp[i+j].insert(num1-num2);
                        if(num2!=0)
                            dp[i+j].insert(num1/num2);
                    }
                }
            }
        }
    }
    for(int i=1; i<9; i++){
        if(dp[i].contains(number)) return i;
    }
    
    return -1;
}