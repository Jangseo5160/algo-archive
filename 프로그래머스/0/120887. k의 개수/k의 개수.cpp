#include <string>
#include <vector>

using namespace std;

int solution(int i, int j, int k) {
    int answer = 0;
    for (int m=i; m<=j; m++){
        string s = to_string(m);
        for(auto c : s){
            if((c-'0')==k){
                answer++;
            }
        }
    }
    return answer;
}