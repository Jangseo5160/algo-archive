#include <string>
#include <set>
#include<iostream>
#include<vector>

using namespace std;

int solution(string dirs) {
    int answer = 0;
    set<pair<int, int>> x;
    set<pair<int, int>> y;

    // vector<vector<bool>> x(11, vector<bool>(11, false));
    // vector<vector<bool>> y(11, vector<bool>(11, false));
    pair<int, int> pos={0,0};
    
    for(auto d: dirs){
        if(d=='U'){
            if(pos.second<5){
                if(!y.contains({pos.first, pos.second})){
                    y.insert({pos.first, pos.second});
                    answer++;
                }
                pos.second+=1;
            }
        }
        else if(d=='D'){
            if(pos.second>-5){
                if(!y.contains({pos.first, pos.second-1})){
                    y.insert({pos.first, pos.second-1});
                    answer++;
                }
                pos.second-=1;
            }
        }
        else if(d=='L'){
            if(pos.first>-5){
                if(!x.contains({pos.first-1, pos.second})){
                    x.insert({pos.first-1, pos.second});
                    answer++;
                }
                pos.first-=1;
            }
        }
        else if(d=='R'){
            if(pos.first<5){
                if(!x.contains({pos.first, pos.second})){
                    x.insert({pos.first, pos.second});
                    answer++;
                }
                pos.first+=1;
            }
        }        
    }
    return answer;
}