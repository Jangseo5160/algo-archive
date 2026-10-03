#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    int n=triangle.size(); //5
    for(int i=n-2; i>=0; i--){ //3,2,1,0
        for(int j=0; j<=i; j++){ // 0123, 012, 01, 0
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1]);
        }
    }
    answer=triangle[0][0];
    return answer;
}