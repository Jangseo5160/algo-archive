#include <string>
#include <vector>

using namespace std;

string solution(string my_string) {
    string answer = "";
    for(auto c:my_string){
        if('A'<=c && c<='Z'){
            answer+=c-'A'+'a';
        }
        else{
            answer+=c-'a'+'A';
        }
    }
    return answer;
}