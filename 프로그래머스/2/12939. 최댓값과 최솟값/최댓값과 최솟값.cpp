#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

string solution(string s) {
    string answer = "";
    vector<int> answ;
    string temp="";
    for(auto a: s){
        if(a==' '){
            answ.push_back(stoi(temp));
            cout<<temp<<" ";
            temp.clear();
        }
        else{
            temp+=a;
        }
    }
    answ.push_back(stoi(temp));
    cout<<temp<<" ";
    int min_v=*min_element(answ.begin(), answ.end());
    int max_v=*max_element(answ.begin(), answ.end());
    answer+=to_string(min_v);
    answer+=" ";
    answer+=to_string(max_v);
    return answer;
}