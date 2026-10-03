#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include<iostream>
using namespace std;

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> ready_q;  //min heap
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> q; //min heap

    for(int i=0; i<jobs.size(); i++){
        ready_q.push({jobs[i][0], jobs[i][1], i}); //요청시간, 수행시간, idx
    }
    int now=0;
    while(!ready_q.empty() || !q.empty()){ //아직 작업 남음
        while(!ready_q.empty() && ready_q.top()[0]<=now){ //레디큐에 남아있는데 현재 시간보다 이전 요청시간 일들
            q.push({ready_q.top()[1],ready_q.top()[0], ready_q.top()[2]}); //수행시간, 요청시간, idx
            ready_q.pop();
        }
        if(q.empty()){//만약 큐가 비어있으면, 레디큐 now는 레디큐 요청시간으로, 둘다 비어있을 순 없음.
           now=ready_q.top()[0];
            continue;
        }
        answer+= (now+q.top()[0] - q.top()[1]);
        now +=q.top()[0];
        q.pop();
    }
    
    
    answer/=jobs.size();
    return answer;
}