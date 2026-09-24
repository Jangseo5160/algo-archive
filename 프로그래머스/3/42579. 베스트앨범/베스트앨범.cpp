#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    unordered_map<string, vector<vector<int>>> playlist;
    vector<pair<int, string>> order;
    
    //playlist 해시맵 만들기
    for(int i=0; i<genres.size(); i++){
        playlist[genres[i]].push_back({plays[i], -i});
    }
    
    for(auto [name, play]: playlist){
        int total=0;
        for (auto p : play){
            total+=p[0];
        }
        order.push_back({total, name});
    }
    
    sort(order.rbegin(), order.rend());
    
    for(auto& p:playlist){
        sort(p.second.rbegin(), p.second.rend());
    }
    
    for(auto [total, name]: order){
        int cnt = 0;
        for(auto song: playlist[name]){
            answer.push_back(-song[1]);
            cnt++;
            if (cnt==2){
                break;
            }
        }
        
    }
    
    return answer;
}