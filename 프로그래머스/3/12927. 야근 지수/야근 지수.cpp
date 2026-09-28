#include <string>
#include <vector>
#include <queue>

using namespace std;

long long solution(int n, vector<int> works) {
    long long answer = 0;
    priority_queue<int> q;
    int sum=0;
    for(auto w:works) {q.push(w); sum+=w;}
    if(sum<=n) return 0;
    while(n>0){
        int curr = q.top();
        q.pop();
        curr--;
        q.push(curr);
        n--;
    }
    while(!q.empty()){
        int cur = q.top();
        q.pop();
        answer+=cur*cur;
    }
    return answer;
}