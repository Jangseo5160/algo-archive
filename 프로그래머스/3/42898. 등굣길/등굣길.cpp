#include <string>
#include <vector>
#include<iostream>
using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    vector<vector<int>> board(n+1, vector<int>(m+1, 0));
    vector<vector<bool>> isPuddle(n+1, vector<bool>(m+1, false));
    
    for(auto p:puddles){
        isPuddle[p[1]][p[0]]=true;
    }
    
    for(int r=1; r<n+1; r++){
        for(int c=1; c<m+1; c++){
            if(r==1 && c==1){
                board[r][c]=1;
                continue;
            }
            if(!isPuddle[r][c]){
                board[r][c] = (board[r-1][c]+board[r][c-1])%1000000007;
            }
            

        }
    }
    return board[n][m];
}