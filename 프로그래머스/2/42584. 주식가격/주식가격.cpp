#include <string>
#include <vector>
#include<stack>
#include<iostream>
using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer(prices.size(), 0);
    stack<int> stk;
    for(int i=0; i<prices.size(); i++){
        if(stk.empty() || prices[stk.top()]<=prices[i])  stk.push(i);
        else{
            while(!stk.empty() && prices[stk.top()]>prices[i]){
                answer[stk.top()]=i-stk.top();
                stk.pop();
            }
            stk.push(i);
        }
    }
    while(!stk.empty()){
        answer[stk.top()] = prices.size()-stk.top()-1;
        stk.pop();
    }
    return answer;
}