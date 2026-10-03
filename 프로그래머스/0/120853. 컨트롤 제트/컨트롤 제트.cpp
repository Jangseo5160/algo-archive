#include <string>
#include <vector>
#include<iostream>
using namespace std;

int solution(string s) {
    int answer = 0;
    vector<int> v;
    int i=0;
    
    while(i<s.size()){
        if(s[i]==' ') {
            i++;
            continue;
        }
        if(s[i]=='Z'){
            if(!v.empty()){
                v.pop_back();
            }
            i++;
            continue;
        }
        
        string temp="";
        while(i<s.size() && s[i]!=' '){
            temp+=s[i];
            i++;
        }
        v.push_back(stoi(temp));
    }
    
    for(auto c:v){
        answer+=c;
    }
    
    return answer;
}