#include <string>
#include <vector>
#include <stack>
#include <cmath>
#include <algorithm>
#include<iostream>
#include<bitset>

using namespace std;

int count_one(int a){
    string s="";
    while(a>0){
        s+=char('0'+a%2);
        a/=2;
    }
    int answer=0;
    for(char c:s){
        if(c=='1') answer++;
    }
    return answer;
}


int solution(int n) {
    int answer = n;
    int cnt= count_one(n);
    
    while(1){
        answer++;
        if(count_one(answer) == cnt) return answer;
    }
}
