#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> lines) {
    int answer = 0;
    vector<int> cnt(201, 0);
    for(auto line: lines){
        for(int x=line[0]; x<line[1]; x++){
            cnt[x+100]++;
        }
    }
    for(int c:cnt){
        if(c>1) answer++;
    }
    
    return answer;
}