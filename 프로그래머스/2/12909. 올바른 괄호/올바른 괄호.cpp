#include<string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    stack<char> stk;
    
    for(auto c:s){
        if(c=='('){
            stk.push(c);
        }
        else{
            if(stk.empty()) return false;
            else{
                if(stk.top()=='(') stk.pop();
            }
        }
    }
    if(stk.empty()) return true;
    else return false;
}