#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> solution(vector<int> num_list, int n) {
    vector<vector<int>> answer;
    for (int j=0; j<num_list.size()/n;j++){
        vector<int> v;
        for (int i=j*n; i<(j+1)*n; i++){
            v.push_back(num_list[i]);
        }
        answer.push_back(v);
    }
    return answer;
}