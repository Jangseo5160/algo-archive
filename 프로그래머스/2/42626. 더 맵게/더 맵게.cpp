#include <string>
#include <vector>
#include<queue>
using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<long long, vector<long long>, greater<long long>> pq(scoville.begin(), scoville.end());
    while(pq.size()>0){
        long long first = pq.top();
        pq.pop();
        if(first>=K) return answer;
        if(pq.empty()) return -1;
        long long second = pq.top();
        pq.pop();  
        pq.push(first+second*2);
        answer++;
    }
    return -1;
}