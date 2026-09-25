#include <string>
#include <vector>

using namespace std;
vector<bool> visited;
int answer;

void dfs(string curr, string target, vector<string>& words, int depth){
    if(curr==target) {
        answer=min(answer, depth);
        return;
    }
    for(int i=0; i<words.size(); i++){
        if(!visited[i]){
            int cnt=0;
            for(int j=0; j<target.size(); j++){
                if(curr[j]!=words[i][j]){
                    cnt++;
                }
            }
            if(cnt==1){
                visited[i]=true;
                dfs(words[i], target, words, depth+1);
                visited[i]=false;
            }
        }
    }
}


int solution(string begin, string target, vector<string> words) {
    visited.assign(words.size(), false);
    answer = 1e9;
    dfs(begin, target, words,0);
    if(answer==1e9){
        return 0;
    }
    return answer;
}