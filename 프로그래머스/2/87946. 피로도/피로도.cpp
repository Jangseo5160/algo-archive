#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    vector<int> order(dungeons.size());
    for(int i=0; i<order.size(); i++)
        order[i]=i; // "몇 번 던전을 어떤 순서로 방문할지"를 표현하는 인덱스 배열
    
    do{
        int cur=k;
        int cnt=0;
        for(int idx:order){
            if(cur>=dungeons[idx][0]){
                cur-=dungeons[idx][1];
                cnt++;
            }
        }
        answer=max(answer, cnt);
    }while(next_permutation(order.begin(), order.end()));
    
    
    return answer;
}