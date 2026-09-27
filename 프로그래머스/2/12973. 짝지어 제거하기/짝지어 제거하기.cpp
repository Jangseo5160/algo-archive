#include <iostream>
#include<string>
#include<stack>

using namespace std;

int solution(string s)
{
    int answer = -1;
    stack<int> stk;
    for(auto t:s){
        if(stk.empty() || stk.top()!=t){
            stk.push(t);
        }
        else if(stk.top()==t){
            stk.pop();
        }
    }
    if(stk.empty()) return 1;
    else return 0;
}