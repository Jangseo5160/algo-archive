#include <string>
#include <vector>
#include<set>
#include<iostream>
using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    multiset<int> s;
    for(auto ope:operations){
        if(ope[0]=='I'){
            ope.erase(0,2);
            s.insert(stoi(ope));
        }
        else if(ope=="D -1"){
            if(!s.empty())
                s.erase(s.begin());
        }
        else{
            if(!s.empty())
                s.erase(prev(s.end()));
        }
    }
    if(s.empty()) return {0,0};
    answer = {*prev(s.end()), *s.begin()};
    return answer;
    // int a=*s.rbegin();
    // cout<<a<<" ";
    // return {a,a};
    // answer = {*s.begin(), *s.rend()};
    // return answer;
}