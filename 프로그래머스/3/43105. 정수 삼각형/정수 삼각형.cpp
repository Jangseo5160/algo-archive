#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    int n = triangle.size();
    vector<vector<int>> dp = triangle;
    for(int i=0; i<n; i++){
        dp[n-1][i] = triangle[n-1][i];
    }
    int k=n-1;
    while (k>0){
        for(int i=0; i<k; i++){
            dp[k-1][i] = max(dp[k][i], dp[k][i+1]) + triangle[k-1][i];
        }
        k--;
    }
    return dp[0][0];
}