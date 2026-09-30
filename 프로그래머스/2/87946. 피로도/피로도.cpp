#include <string>
#include <vector>
#include<algorithm>
using namespace std;

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    vector<int> order(dungeons.size());
    for(int i=0; i<dungeons.size(); i++){
        order[i]=i;
    }
    do{
        int cnt=0;
        int cur = k;
        for(auto a: order){
            if(cur>=dungeons[a][0]){
                cur-=dungeons[a][1];
                cnt++;
            }
        }
        answer = max(answer, cnt);
    }while(next_permutation(order.begin(), order.end()));
    return answer;
}