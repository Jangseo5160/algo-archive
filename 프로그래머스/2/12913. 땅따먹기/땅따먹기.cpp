#include <iostream>
#include <vector>
using namespace std;

int solution(vector<vector<int> > land)
{
    int answer = 0;
    int n=land.size();
    for(int r=n-1; r>0; r--){
        land[r-1][0]+=max(land[r][1], max(land[r][2], land[r][3]));
        land[r-1][1]+=max(land[r][0], max(land[r][2], land[r][3]));
        land[r-1][2]+=max(land[r][1], max(land[r][0], land[r][3]));
        land[r-1][3]+=max(land[r][1], max(land[r][2], land[r][0]));
        }
    answer=max(land[0][0], max(land[0][1], max(land[0][2], land[0][3])));

    return answer;
}