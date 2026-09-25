#include <string>
#include <vector>
#include <queue>
using namespace std;
vector<bool> visited; 


int solution(vector<int> numbers, int target) {
    int answer = 0;
    queue<int> q;
    q.push(0);
    
    for(int num: numbers){
        int size = q.size();
        
        for(int i=0; i<size; i++){           
            q.push(q.front()+num);
            q.push(q.front()-num);
            q.pop();
        }
    }
    while(!q.empty()){
        int x = q.front();
        if(x==target){
            answer++;
        }
        q.pop();
    }
    return answer;
}