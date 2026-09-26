#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int solution(vector<string> arr)
{
    int answer = -1;
    int n=(arr.size()+1)/2;
    vector<vector<int>> mindp(n, vector<int>(n, 1000000000));
    vector<vector<int>> maxdp(n, vector<int>(n, -1000000000));
    for(int i=0; i<n; i++){
        mindp[i][i] = stoi(arr[i*2]);
        maxdp[i][i] = stoi(arr[i*2]);
    }
    for(int length=1; length<n; length++){
        for(int start=0; start<n-length; start++){
            int end=start+length;
            for(int k=start; k<end; k++){
                if(arr[k*2+1]=="-"){
                    mindp[start][end]=min(mindp[start][end], mindp[start][k]-maxdp[k+1][end]);
                    maxdp[start][end]=max(maxdp[start][end], maxdp[start][k]-mindp[k+1][end]);
                }
                if(arr[k*2+1]=="+"){
                    mindp[start][end]=min(mindp[start][end], mindp[start][k]+mindp[k+1][end]);
                    maxdp[start][end]=max(maxdp[start][end], maxdp[start][k]+maxdp[k+1][end]);                
                }
            }
        }
    }
    answer = maxdp[0][n-1];
    return answer;
}