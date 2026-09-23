#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> array) {
    vector<int> cnt(1001,0);
    for(int a: array){
        cnt[a]++;
    }
    int idx = max_element(cnt.begin(), cnt.end())-cnt.begin();
    for(int i=0;i<cnt.size();i++){
        if (i!=idx && cnt[i]==cnt[idx]){
            return -1;
        }
    }
    return idx;
}