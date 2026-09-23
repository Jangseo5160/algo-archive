#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(string s) {
    string answer = "";
    
    for (char a = 'a'; a <='z';a++){
        if (count(s.begin(), s.end(), a)==1){
            answer+=a;
        }
    }
    
    return answer;
}