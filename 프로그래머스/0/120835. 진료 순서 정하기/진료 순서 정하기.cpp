#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> emergency) {
    vector<int> answer;
    vector<int> temp = emergency;
    sort(temp.rbegin(), temp.rend());
    for(auto a: emergency){
        for(int i=0; i<temp.size(); i++){
            if (temp[i] == a){
                answer.push_back(i+1);
            }
        }
    }
    return answer;
}