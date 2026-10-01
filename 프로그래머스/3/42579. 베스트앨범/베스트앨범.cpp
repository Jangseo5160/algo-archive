#include <string>
#include <vector>
#include<unordered_map>
#include<algorithm>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    unordered_map<string, vector<pair<int, int>>> mp;
    unordered_map<string, int> gen;
    
    for(int i=0; i<genres.size(); i++){
        gen[genres[i]]+=plays[i];
    }
    
    vector<pair<int, string>> temp;
    for(auto& [category, total]:gen){
        temp.push_back({total, category});
    }
    sort(temp.rbegin(), temp.rend());
    
    
    for(int i=0; i<genres.size(); i++){
        mp[genres[i]].push_back({plays[i], i});
    }
    for(auto& [category, songs]:mp){
        sort(songs.begin(), songs.end(), [](const auto&a, const auto&b){
            if(a.first==b.first) return a.second<b.second;
            return a.first>b.first;
        });
    }
    
    for(auto& a:temp){
        int cnt=0;
        string cate = a.second;
        for(auto& [playcnt, idx]: mp[cate]){
            if(cnt>=2) break;
            answer.push_back(idx);
            cnt++;
        }
    }
    
    return answer;
}