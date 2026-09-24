#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer(prices.size(), 0);
    stack<int> s;
    for(int i=0; i<prices.size(); i++){
        while(!s.empty() && prices[s.top()]>prices[i]){
            int idx = s.top();
            s.pop();
            answer[idx] = i-idx;
        }
        s.push(i);
    }
    while(!s.empty()){
        int idx = s.top();
        s.pop();
        answer[idx] = prices.size()-1-idx;
    }
    return answer;
}