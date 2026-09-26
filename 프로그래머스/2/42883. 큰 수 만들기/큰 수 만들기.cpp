#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <iostream>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    stack<char> stk;
    for(auto n:number){
        if(stk.empty() || stk.top()>=n || k<=0){
            stk.push(n);
        }
        else{
            while(!stk.empty() && stk.top()<n && k>0){
                stk.pop();
                k--;
            }
            stk.push(n);
        }
        
    }
    while(k>0){
        stk.pop();
        k--;
    }
    while(!stk.empty()){
        answer+=stk.top();
        stk.pop();
    }
    reverse(answer.begin(), answer.end());
    
    return answer;
}