#include <string>
#include <vector>

using namespace std;

int solution(vector<string> s1, vector<string> s2) {
    int answer = 0;
    for(auto s:s1){
        for (auto c:s2){
            if(s==c){
                answer+=1;
            }
        }
    }
    return answer;
}