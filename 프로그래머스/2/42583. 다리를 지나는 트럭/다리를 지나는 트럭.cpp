#include <string>
#include <vector>
#include<queue>

using namespace std;

//queue에 시각 입력
//현재시간-queue front ==brdige_length 라면 pop

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    int i=0;
    int cur=0;
    int sum=0;
    queue<vector<int>> q;
    while(!q.empty() || i<truck_weights.size()){ //i=0,1,2,3
        if(i<truck_weights.size() && sum+truck_weights[i]<=weight){ //7<=10
            sum+=truck_weights[i]; //7
            q.push({cur, i}); //{0,0}
            i++;
        }
        
        cur++; //1
        if(!q.empty() && cur-q.front()[0]==bridge_length) { //2초
            sum-=truck_weights[q.front()[1]];
            q.pop();
        }
    }
    answer=cur+1;
    return answer;
}