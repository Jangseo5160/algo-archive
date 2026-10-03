#include <string>
#include <vector>
#include<iostream>
#include <algorithm>
using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    vector<vector<int>> board(n+1, vector<int>(m+1, 0));
    
    
    
    for(int r=1; r<n+1; r++){
        for(int c=1; c<m+1; c++){
            if(r==1 && c==1){
                board[r][c]=1;
                continue;
            }
            bool flag=false;
            if(find(puddles.begin(), puddles.end(), vector<int>{c, r})==puddles.end())
                board[r][c] = (board[r-1][c]+board[r][c-1])%1000000007;

        }
    }
    return board[n][m];
}