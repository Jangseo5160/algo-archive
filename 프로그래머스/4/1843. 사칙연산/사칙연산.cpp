#include <vector>
#include <string>
using namespace std;

int solution(vector<string> arr)
{
    int answer = -1;
    int n=(arr.size()+1)/2; //4
    vector<vector<int>> mindp(n, vector<int>(n, 1e9));
    vector<vector<int>> maxdp(n, vector<int>(n, -1e9));
    
    for(int i=0;i<n; i++){
        mindp[i][i]=stoi(arr[i*2]);
        maxdp[i][i]=stoi(arr[i*2]);
    }
    
    for(int len=1; len<n; len++){
        for(int i=0; i+len<n; i++){
            int j=i+len;
            for(int k=i; k<j; k++){
                if(arr[k*2+1]=="-"){ //1, 3, 5,  012
                    mindp[i][j]=min(mindp[i][j], mindp[i][k]-maxdp[k+1][j]);
                    maxdp[i][j]=max(maxdp[i][j], maxdp[i][k]-mindp[k+1][j]);
                }
                else{
                    mindp[i][j]=min(mindp[i][j], mindp[i][k]+mindp[k+1][j]);
                    maxdp[i][j]=max(maxdp[i][j], maxdp[i][k]+maxdp[k+1][j]);
                }
            }
        }
    }
    
    
    
    return maxdp[0][n-1];
}