#include <string>
#include <vector>

using namespace std;

int solution(int k, vector<int> tangerine) {
    vector<int> cnt(10000001,0);
    for(int x:tangerine){
        cnt[x]++;
    }
    vector<int> frequency(tangerine.size()+1, 0);
    for(int x: cnt){
        if(x>0){
            frequency[x]++;
        }
    }
    int answer=0;
    for(int i = tangerine.size(); i>=1; i--){
        while (frequency[i]>0){
            k-=i;
            answer++;
            frequency[i]--;
            
            if(k<=0){
                return answer;
            }
        }
    }
    return answer;
}