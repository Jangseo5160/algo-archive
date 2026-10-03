#include <string>
#include <vector>
#include <stack>
using namespace std;

int solution(string word) {
    int answer = 0;
    stack<string> stk;
    string ori = "AEIOU";
    stk.push("");
    int cnt=-1;
    while(!stk.empty()){ //u o i e a au ao ai ae aa aao.. aaae
        string cur = stk.top();
        stk.pop();
        cnt++;
        if(cur==word) return cnt;
        if(cur.size()==5) continue;
        for(int i=4; i>=0; i--){
            stk.push(cur+ori[i]);
        }
    }
    
    
    return answer;
}