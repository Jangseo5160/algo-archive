#include <string>
#include <vector>

using namespace std;

int solution(string name) {
    int answer = 0;
    
    for(auto n:name){
        int up = n-'A';
        int down = 'Z'-n+1;
        answer+=min(up, down);
    }
    int move = name.size()-1;
    
    for(int i=0; i<name.size(); i++){
        int next = i+1;
        while(next<name.size() && name[next]=='A'){
            next++;
        }
        int left_back = (name.size()-next)*2 + i;
        int right_back = i+i+name.size()-next;
        move = min(move, min(left_back, right_back));
    }
    answer+=move;
    return answer;
}