#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string my_string) {
    string answer = "";
    for(auto a:my_string){
        if (find(answer.begin(), answer.end(), a)==answer.end()){
            answer+=a;
        }
    }
    return answer;
}