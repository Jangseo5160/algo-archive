#include <vector>
#include <iostream>
#include <stack>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    stack<int> s;
    for(auto a: arr){
        if(s.empty() || s.top()!=a){
            s.push(a);
        }
    }
    while(!s.empty()){
        int t = s.top();
        answer.push_back(t);
        s.pop();
    }
    reverse(answer.begin(), answer.end());
    return answer;
}