#include <string>
#include <vector>

using namespace std;
vector<string> words;
string W = "AEIOU";

void dfs(string s){
    if(s.size()>5) return;
    
    if(!s.empty())
        words.push_back(s);
        
    for(auto w:W){
        dfs(s+w);
    }
}

int solution(string word) {
    int answer = 0;
    dfs("");
    for(int i=0; i<words.size(); i++){
        if(words[i]==word){
            return i+1;
        }
    }
    return -1;
}