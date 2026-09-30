#include <string>
#include <vector>
#include<queue>
#include<algorithm>
#include<iostream>
using namespace std;

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
    sort(jobs.begin(), jobs.end());
    int i=0;
    int now =0;
    while(i<jobs.size() || !pq.empty()){
        if(pq.empty() && i<jobs.size())
            now = max(now, jobs[i][0]);

        while(i<jobs.size() && jobs[i][0]<=now){
            pq.push({jobs[i][1], jobs[i][0], i});
            i++;
        }
        
        if(!pq.empty()){
            vector<int> new_j = pq.top();
            pq.pop();
            
            now += new_j[0];
            answer+=(now-new_j[1]);
        }
    }
    
    while(!pq.empty()){
        vector<int> new_j = pq.top();
        pq.pop();
        now += new_j[0];
        answer+=(now-new_j[1]);
    }
    answer=answer/jobs.size();
    return answer;
}