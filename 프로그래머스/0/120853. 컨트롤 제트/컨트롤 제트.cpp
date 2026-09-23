#include <string>
#include <vector>
#include <sstream>
using namespace std;

int solution(string s) {
    int answer = 0;
    vector<string> word;
    string temp;
    stringstream ss(s);
    
    while (ss>>temp){
        word.push_back(temp);
    }
    for(int i=0; i<word.size(); i++){
        if(i<word.size()-1 && word[i+1]=="Z"){
            i++;
        }
        else answer+=stoi(word[i]);
    }
    return answer;
}