#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> v;
    for(auto n:numbers){
        v.push_back(to_string(n));
    }
    sort(v.begin(), v.end(), [](string a, string b){
        return a+b>b+a;
    });
    for(auto a:v){
        answer+=a;
    }
    if(answer[0] == '0') return "0";
    return answer;
}