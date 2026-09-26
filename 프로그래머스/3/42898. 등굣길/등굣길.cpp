#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    vector<vector<long long>> board(n+1, vector<long long>(m+1,0));
    
    for(int r=1; r<=n; r++){
        for(int c=1; c<=m; c++){
            if(r==1 && c==1) board[r][c]=1;
            else if(find(puddles.begin(), puddles.end(), vector<int>{c, r})!=puddles.end()) continue;
            else{
                board[r][c] = (board[r-1][c]+board[r][c-1])%1000000007;
            }
        }
    }
    answer = board[n][m];
    return answer;
}