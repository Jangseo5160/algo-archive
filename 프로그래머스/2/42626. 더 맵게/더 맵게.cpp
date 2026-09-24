#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> pq;
    for(auto a: scoville) pq.push(a);
    int cnt=0;
    while(!pq.empty()){
        if(pq.top()<K){
            int b = pq.top();
            pq.pop();
            
            if(pq.empty()) return -1;
            
            int c = pq.top();
            pq.pop();
            pq.push(b+c*2);
            cnt++;

        }
        else{
            return cnt;
        }
    }
}