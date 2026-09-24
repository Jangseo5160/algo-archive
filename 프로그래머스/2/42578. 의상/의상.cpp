#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map <string, int> mp;
    for(int i=0; i<clothes.size(); i++){
        string category = clothes[i][1];
        string cloth = clothes[i][0];
        mp[category]++;
    }
    for(auto a:mp){
        answer *= (a.second+1);
    }
    return answer-1;
}