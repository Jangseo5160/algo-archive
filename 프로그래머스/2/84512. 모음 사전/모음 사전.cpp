#include <string>
#include <vector>
#include<stack>
using namespace std;

int solution(string word) {
    int answer = 0;
    stack<string> stk;
    string s="AEIOU";
    int cnt=0;
    stk.push("");
    
    while(!stk.empty()){
        string cur = stk.top();
        stk.pop();
        cnt++;
        
        if(cur==word) return cnt-1;
        if(cur.size()==5) continue;
        for(int i=4; i>=0;i--){
            stk.push(cur+s[i]);
        }
    }
    answer = cnt;
    return answer;
}