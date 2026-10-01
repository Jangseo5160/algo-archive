#include <string>
#include <vector>
#include<algorithm>
using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) {
    int answer = 0;
    vector<vector<int>> v(n+1, vector<int>(m+1, 0));
    
    for(int c=1; c<m+1; c++){
        for(int r=1; r<n+1; r++){
            if(r==1 && c==1) {v[1][1]=1; continue;}
            if(find(puddles.begin(), puddles.end(), vector<int>{c, r})!=puddles.end()) continue;
            v[r][c] = (v[r-1][c] + v[r][c-1])%1000000007;
        }
    }
    answer = v[n][m]%1000000007;
    return answer;
}