#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
    vector<vector<int>> answer(arr1.size());
    for(int r=0; r<arr1.size(); r++){
        for(int cc=0; cc<arr2[0].size(); cc++){
            int temp=0;
            for(int rr=0; rr<arr2.size(); rr++){
                temp+=arr1[r][rr]*arr2[rr][cc];
            }
            answer[r].push_back(temp);
        }
    }
    return answer;
}