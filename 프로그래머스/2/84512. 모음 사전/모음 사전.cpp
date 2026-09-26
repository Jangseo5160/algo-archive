#include <string>
#include <vector>

using namespace std;
int cnt=0;
vector<char> w = {'A', 'E', 'I', 'O', 'U'};
bool found = false;
int answer = 0;

void dfs(string& word, string curr){
    if(found) return;
    
    if(curr.size()==5){
        return;
    }
    for(auto a:w){
        string next = curr+a;
        cnt++;
        if(next==word){
            answer=cnt;
            found=true;
            return;
        }
         dfs(word, next);
    }
}


int solution(string word) {
    dfs(word, "");
    return answer;
}