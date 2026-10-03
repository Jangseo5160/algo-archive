#include <string>
#include <vector>
#include<stack>
using namespace std;

int solution(string word) {
    int answer = 0;
    stack<string> stk;
    string ori="AEIOU";
    int cnt=0;
    stk.push("");
    while(!stk.empty()){
        string cur=stk.top();
        stk.pop();
        
        if(cur.size()>5){
            continue;
        }
        if(!cur.empty()){
            cnt++;
            if(cur==word) return cnt;
        }
        for(int i=4; i>=0; i--){
            stk.push(cur+ori[i]);
        }
    }
    
    return answer;
}