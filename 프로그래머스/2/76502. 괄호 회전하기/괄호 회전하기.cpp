#include <string>
#include <vector>
#include <stack>
#include <iostream>
using namespace std;

int solution(string s) {
    int answer = 0;
    
    int k=s.size();
    while(k>0){
        stack<char> stk;
        bool can=true;
        for(int i=0; i< s.size(); i++){
            if(s[i]=='[' ||s[i]=='(' ||s[i]=='{'){
                stk.push(s[i]);
            }
            else if(stk.empty() && (s[i]==']'||s[i]==')'||s[i]=='}')) {can=false; break;}
            else if(s[i]==']'){
                if(stk.top() == '[') stk.pop();
                else {can=false; break;}
            }
            else if(s[i]==')'){
                if(stk.top() == '(') stk.pop();
                else {can=false; break;}
            }
            else if(s[i]=='}'){
                if(stk.top() == '{') stk.pop();
                else {can=false; break;}
            }
        }
        if (can){
            if(stk.empty()) answer++;
        }
        
        k--;
        char temp = s[0];
        s.erase(s.begin());
        s = s+temp;
    }
    return answer;
}