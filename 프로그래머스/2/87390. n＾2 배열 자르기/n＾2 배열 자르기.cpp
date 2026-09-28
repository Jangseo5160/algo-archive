#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int n, long long left, long long right) {
    vector<int> answer;
    
    long long sc=left%n;
    long long sr=left/n;
    long long ec=right%n;
    long long er=right/n;
    // cout<<sr<<sc<<er<<ec;
    if(sr==er){
        for(long long tsc=sc; tsc<=ec; tsc++){
            answer.push_back(max(tsc+1, sr+1));
        }
        return answer;
    }
    
    for(long long tsc=sc; tsc<n; tsc++){
        answer.push_back(max(tsc+1, sr+1));
        
    }
    
    for(long long i=sr+1; i<er; i++){
        for(long long j=0; j<n; j++){
            answer.push_back(max(i+1, j+1));
        }
    }
    
    for(long long tec=0; tec<=ec; tec++){
        answer.push_back(max(tec+1, er+1));
    }
    
    return answer;
}