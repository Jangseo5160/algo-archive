#include <string>
#include <vector>
#include<algorithm>
#include<iostream>
using namespace std;

string solution(vector<int> numbers) {
    string answer = "";
    sort(numbers.begin(), numbers.end(), [](auto&a, auto& b){
        string sa = to_string(a);
        string sb= to_string(b);
        return sa+sb>sb+sa;
    });
    
    for(auto n:numbers){
        answer+=to_string(n);
    }
    if(answer[0]=='0') return "0";
    return answer;
}