#include <string>
#include <vector>

using namespace std;

string solution(string my_string) {
    string answer = "";
    string list = "aeiou";
    for(auto s:my_string){
        if(s!=list[0] && s != list[1] && s!=list[2] && s != list[3]&&s!=list[4]){answer+=s;}
    }
    return answer;
}