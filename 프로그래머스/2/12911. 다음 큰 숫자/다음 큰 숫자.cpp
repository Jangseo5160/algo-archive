#include <string>
#include <vector>
#include <stack>
#include <cmath>
#include <algorithm>
#include<iostream>
using namespace std;

string conv(int a){
    // stack<string> stk;
    // string answer="";
    // while(a>0){
    //     stk.push(to_string(a%2));
    //     a/=2;
    // }
    // while(!stk.empty()){
    //     answer+=stk.top();
    //     stk.pop();
    // }
    // return answer;
    string s;
    while(a>0){
        s+=char('0'+a%2);
        a/=2;
    }
    reverse(s.begin(), s.end());
    return s;
}

int conv_int(string s){
    int answer=0;
    // for(int i=0; i<s.size(); i++){
    //     if(s[i]=='1')
    //     {
    //         int j=s.size()-1-i;
    //         answer+=pow(2,j);
    //     }
    // }
    for(char c:s){
        answer = answer*2 + (c-'0');
    }
    return answer;
}

int solution(int n) {
    int answer = 0;
    string a = conv(n);
    a="0"+a;
    for(int i=a.size()-1; i>=1; i--){
        if(a[i]=='1' && a[i-1]=='0'){
            swap(a[i], a[i-1]);
            sort(a.begin()+i+1, a.end());
            return conv_int(a);
        }
    }
}