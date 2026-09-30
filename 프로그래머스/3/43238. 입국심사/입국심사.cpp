#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    long long right = (long long)(*max_element(times.begin(), times.end())) * n;
    long long left=0;
    
    while(left<right){
        long long mid=(right+left)/2;
        long long cnt=0;
        for(auto t:times){
            cnt+=mid/t;
        }
        if(cnt>=n){
            right=mid;
        }
        else{
            left=mid+1;
        }
        if(left==right) break;
    }
    answer=right;
    return answer;
}