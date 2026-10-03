#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> ready; //요청 시점, 작업소요시간, 작업번호
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> doing; //작업소요시간, 요청시각, 작업번호
    
    for(int i=0; i<jobs.size(); i++){
        ready.push({jobs[i][0], jobs[i][1], i});
    }
    
    int now=0;
    
    while(!doing.empty() || !ready.empty()){
        while(!ready.empty() && ready.top()[0]<=now){
            doing.push({ready.top()[1], ready.top()[0], ready.top()[2]});
            ready.pop();
        }
        if(doing.empty()){
            now = ready.top()[0];
            continue;
        }
        int dur = doing.top()[0];
        int start = doing.top()[1];
        now +=dur;
        answer += (now-start);
        doing.pop();
        
    }
    answer/=jobs.size();
    return answer;
}