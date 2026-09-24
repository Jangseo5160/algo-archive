#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string, int> mp;
    for(auto s:participant){
        mp[s]++;
    }
    
    for(auto s:completion){
        mp[s]--;
    }
    
    for(auto s:mp){
        if(s.second>0) return s.first;
    }
    return answer;
}