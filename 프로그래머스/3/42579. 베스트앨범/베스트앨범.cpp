#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include<iostream>
using namespace std;

/*
카테고리별 플레이 횟수 더하기 => 정렬하기 => unordered_map, vector에 value, key 순으로 삽입
각 카테고리별 최대 횟수 두개 꺼내기, 고유번호 기억해서 낮은거 먼저 수록
장르에 속한 곡이 하나라면 하나만 선택
*/
vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    unordered_map<string, int> mp;
    
    for(int i=0; i<genres.size(); i++){
        mp[genres[i]]+=plays[i];
    }
    vector<pair<int, string>> temp; //꺼내야할 카테고리대로 정렬
    for(auto& [key, value]:mp){
        temp.push_back({value, key});
    }
    sort(temp.begin(), temp.end(), [](auto& a, auto& b){
        return a.first>b.first;
    });
    
    unordered_map<string, vector<pair<int, int>>> songs;
    
    for(int i=0; i<genres.size(); i++){
        songs[genres[i]].push_back({plays[i],i});
    }
    for(auto& [key, value]:songs){
        sort(value.begin(), value.end(), [](auto& a, auto& b){ //
            if(a.first == b.first) return a.second<b.second;
            return a.first>b.first;
        });
    }
    
    for(auto& t:temp){ 
        string key = t.second;
        answer.push_back(songs[key][0].second);
        if(songs[key].size()>=2){
            answer.push_back(songs[key][1].second);
        }
    }
    
    return answer;
}