#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> pq;
    for(auto a: scoville) pq.push(a);
    int cnt=0;
    while(pq.top()<K){
        if(pq.size()==1) return -1;
        int b = pq.top();
        pq.pop();           
        int c = pq.top();
        pq.pop();
        pq.push(b+c*2);
        cnt++;
    }
    return cnt;
}