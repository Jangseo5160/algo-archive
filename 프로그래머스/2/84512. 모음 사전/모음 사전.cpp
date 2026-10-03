#include <string>
#include <vector>

using namespace std;
int answer=0;
string W="AEIOU";
int cnt=0;
void dfs(string s, auto& word){
    if(s.size()>5) return;
    if(!s.empty()){
        cnt++;
        if(s==word){
            answer=cnt;
            return;
        }
    }
    for(auto w:W){
        dfs(s+w, word);
        if(answer!=0) return;
        
    }
}

int solution(string word) {
    dfs("", word);
    return answer;
}