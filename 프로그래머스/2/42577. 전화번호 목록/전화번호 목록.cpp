#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    unordered_set <string> number;
    
    for(auto s:phone_book){
        number.insert(s);
    }
    for(auto num: number){
        string prefix = "";
        for (int i=0; i<num.size()-1;i++){
            prefix+=num[i];
            if(number.contains(prefix)){
                return false;
            }
        }
    }
    return true;
}