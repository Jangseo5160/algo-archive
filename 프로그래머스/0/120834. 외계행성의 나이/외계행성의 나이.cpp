#include <string>
#include <vector>

using namespace std;

string solution(int age) {
    string answer = "";
    string s = to_string(age); //"23"
    for(auto a:s){//"2"
        answer+='a'+(a-'0');//'a'+2
    }
    return answer;
}