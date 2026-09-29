#include <string>
#include <vector>
#include<unordered_map>
#include<queue>
#include<iostream>
using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    vector<int> nums;
    unordered_map<int, int> m;
    for(int i=0; i<s.size(); i++){
        if(s[i]!='}' && s[i]!='{' && s[i]!=','){
            string temp="";
            while (s[i]!='}' && s[i]!='{' && s[i]!=','){
                temp+=s[i];
                i++;
            }
            nums.push_back(stoi(temp));
        }
    }
    
    for(auto a: nums){
        m[a]++;
    }
    priority_queue<pair<int, int>> pq;
    for(auto [a,b]: m){
        pq.push({b, a});
    }
    while (!pq.empty()){
        auto a=pq.top();
        pq.pop();
        answer.push_back(a.second);
    }
    return answer;
}