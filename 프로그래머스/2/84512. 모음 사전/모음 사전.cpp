#include <string>
#include <vector>

using namespace std;
vector<string> alpha = {"A", "E", "I", "O", "U"};
int answer = 0;
int cnt =0;

void dfs(string curr, const string& word ){
    if(curr.size()>5){
        return;
    }
    if(!curr.empty()){
        cnt++;
        if(curr == word){
            answer=cnt;
            return;
        }
    }

    for(auto a: alpha){
        dfs(curr+a, word);
        // if(answer!=0) return;
    }
}


int solution(string word) {
    dfs("", word);
    
    return answer;
}