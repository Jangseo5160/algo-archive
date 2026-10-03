#include <string>
#include <vector>

using namespace std;
int answer=0;
string ori="AEIOU";
int cnt=0;
void dfs(string s, const auto& word){
    if(s.size()>5) return;
    
    if(!s.empty()){
        cnt++;
        if(s==word) {
            answer=cnt;
            return;
        }
    }
    
    for(auto c:ori){
        dfs(s+c, word);
    }
}


int solution(string word) {
    dfs("", word);
    return answer;
}