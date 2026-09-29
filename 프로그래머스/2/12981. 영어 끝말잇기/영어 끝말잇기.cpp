#include <string>
#include <vector>
#include <iostream>
#include<unordered_map>
using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    unordered_map<string, int> m;
    int order =0; int cnt=0;
    m[words[0]]++;
    for(int i=1; i<words.size(); i++){
        if(m[words[i]]!=0 || words[i][0]!=words[i-1][words[i-1].size()-1]){
            order = (i%n)+1;
            cnt = (i/n)+1;
            break;
        } //wrong
        m[words[i]]++;
    }
    answer.push_back(order);
    answer.push_back(cnt);
    return answer;
}