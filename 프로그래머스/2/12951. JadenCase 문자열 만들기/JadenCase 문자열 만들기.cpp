#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    for(int i=0; i<s.size(); i++){
        char c = s[i];
        
        if(i==0 || s[i-1]== ' '){
            if(c>='a' && c<'z'){
                c=c-'a'+'A';
            }
        }
        else{
            if(c>='A' && c<='Z'){
                c=c-'A'+'a';
            }
        }
        answer+=c;
    }
    return answer;
}