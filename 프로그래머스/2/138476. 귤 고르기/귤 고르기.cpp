#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int solution(int k, vector<int> tangerine) {
    int answer = 0;
    unordered_map<long long, int> m;
    for(auto t:tangerine){
        m[t]++;
    }
    vector<int> cnt;
    for(auto& [key, v]:m){
        cnt.push_back(v);
    }
    sort(cnt.rbegin(), cnt.rend());
    int i=0;
    while(k>0){
        k-=cnt[i];
        answer++;
        i++;
    }
    return answer;
}