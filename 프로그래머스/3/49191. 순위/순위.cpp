#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    vector<vector<int>> board(n, vector<int>(n, 0));
    
    for(auto r:results){
        board[r[0]-1][r[1]-1]=1;
    }
    
    for(int k=0; k<n; k++){
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(board[i][k]==1 && board[k][j]==1) board[i][j]=1;
            }
        }
    }
    
    for(int i=0; i<n; i++){
        int cnt=0;
        for(int j=0; j<n; j++){
            if(board[i][j]==1 || board[j][i]==1) cnt++;
        }
        if(cnt==n-1) answer++;
    }
    
    return answer;
}