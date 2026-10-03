#include <string>
#include <vector>
#include<algorithm>
#include<set>
#include<iostream>
using namespace std;

bool isPrime(int a){
    if(a<2) return false;
    for(int i=2; i*i<=a; i++){
        if(a%i==0) return false;
    }
    return true;
}

int solution(string numbers) {
    int answer = 0;
    sort(numbers.begin(), numbers.end());
    set<int> s;
    do{
        string temp="";
        for(auto c:numbers){
            temp+=c;
            s.insert(stoi(temp));
        }
    }while(next_permutation(numbers.begin(), numbers.end()));
    
    for(auto t:s){
        if(isPrime(t)) answer++;
    }
    
    return answer;
}