#include <string>
#include <vector>

using namespace std;

int solution(string my_string) {
    int answer = 0;
    for(auto s:my_string){
        if(isdigit(s)){
            answer+=s-'0';
        }
    }
    return answer;
}