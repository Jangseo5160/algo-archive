#include <string>
#include <vector>

using namespace std;
//가위2, 바위 0, 보 5
string solution(string rsp) {
    string answer = "";
    for(auto s:rsp){
        if(s=='2') answer+='0';
        else if(s=='0') answer+='5';
        else answer+='2';
    }
    return answer;
}