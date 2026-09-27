#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<int> topping) {
    int answer = 0;
    unordered_map<int, int> map;
    for(auto t:topping){
        map[t]++;
    }
    int n=map.size();
    unordered_map<int, int> first;
    unordered_map<int, int> second=map;
    
    for(int i=0; i<topping.size(); i++){
        first[topping[i]]++;
        if(second[topping[i]]>0){
            second[topping[i]]--;
            if(second[topping[i]]==0) second.erase(topping[i]);
        }
        if(first.size() == second.size()){
            answer++;
        }
        if(first.size()>second.size()) break;
    }
    return answer;
}