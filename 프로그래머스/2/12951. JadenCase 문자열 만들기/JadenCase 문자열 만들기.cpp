#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    for(int i=0; i<s.size(); i++){
        if(i==0){
            if(isdigit(s[i])) answer+=s[i];
            else answer+=toupper(s[i]);
        }
        else if(s[i]==' ')
            answer+=s[i];
        
        else if(s[i-1]==' ')
            answer+=toupper(s[i]);
        else
            answer+=tolower(s[i]);
    }
    return answer;
}