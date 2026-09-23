#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(string my_string) {
    vector<int> answer;
    for(auto s:my_string){
        if(isdigit(s)){
            answer.push_back(s-'0');
        }
    }
    sort(answer.begin(), answer.end());
    return answer;
}