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
            v.push_back(1500);
            i++;
            continue;
        }
        string temp="";
        while(i<s.size() && s[i]!=' '){
            temp+=s[i];
            i++;
        }
        cout<<temp<<" ";
        v.push_back(stoi(temp));
    }
    
    for(int i=0; i<v.size(); i++){
        if(v[i+1]==1500 || v[i]==1500) continue;
        else{
            answer+=v[i];
            cout<<answer<<" ";
        }
    }
    
    return answer;
}