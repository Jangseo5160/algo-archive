#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for(auto a:commands){
        int i=a[0]-1;
        int j=a[1];
        int k=a[2];
        vector<int> temp;
        for(int m=i; m<j; m++){
            temp.push_back(array[m]);
        }
        sort(temp.begin(), temp.end());
        answer.push_back(temp[k-1]);
    }
    return answer;
}