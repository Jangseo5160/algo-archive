#include <string>
#include <vector>
#include <stack>
#include <cmath>
#include <algorithm>
#include<iostream>
#include<bitset>

using namespace std;

// string conv(int a){
//     int s=0;
//     while(a>0){
//         s+=char('0'+a%2);
//         a/=2;
//     }
//     reverse(s.begin(), s.end());
//     return s;
// }

// int conv_int(string s){
//     int answer=0;
//     for(char c:s){
//         answer = answer*2 + (c-'0');
//     }
//     return answer;
// }

int solution(int n) {
    int answer = n;
    int cnt= bitset<32>(n).count();
    
    while(1){
        answer++;
        if(bitset<32>(answer).count() == cnt) return answer;
    }
}
