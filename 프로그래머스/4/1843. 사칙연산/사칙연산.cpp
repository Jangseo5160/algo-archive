#include <vector>
#include <string>
using namespace std;

int solution(vector<string> arr)
{
    int answer = -1;
    int n = (arr.size()+1)/2;
    vector<vector<int>> mindp(n, vector<int>(n,1000000));
    vector<vector<int>> maxdp(n, vector<int>(n,-1000000));
    
    for(int i=0; i<n; i++){
        mindp[i][i]=stoi(arr[i*2]);
        maxdp[i][i]=stoi(arr[i*2]);
    }
    for(int l=1; l<n; l++){
        for(int i=0; i<n-l; i++){
            int j=i+l;
            for(int k=i; k<j; k++){
               if(arr[k*2+1]=="-"){
                    maxdp[i][j] = max(maxdp[i][j] , maxdp[i][k] - mindp[k+1][j]);
                    mindp[i][j] = min(mindp[i][j] ,mindp[i][k] - maxdp[k+1][j]);
                }
                else{
                    maxdp[i][j] = max(maxdp[i][j] , maxdp[i][k] + maxdp[k+1][j]);
                    mindp[i][j] = min(mindp[i][j] ,mindp[i][k] + mindp[k+1][j]);
                }
            }

        }
    }

    return maxdp[0][n-1];
}