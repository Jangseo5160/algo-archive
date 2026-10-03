#include <string>
#include <vector>
#include<set>
using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    set<string> book;
    for(auto p:phone_book){
        book.insert(p);
    }
    for(auto num:book){
        string temp="";
        for(int i=0; i<num.size()-1; i++){
            temp+=num[i];
            if(book.contains(temp)) return false;
        }
    }
    
    
    
    return true;
}