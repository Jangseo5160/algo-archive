#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    long long left = 0;
    long long right = *max_element(times.begin(), times.end());
    right *= n;
    while(left<=right){
        long long mid = (left+right)/2;
        long long cnt=0;
        for(auto t:times){
            cnt+=mid/t;
        }
        if(cnt<n){
            left=mid+1;
        }
        else{
            right=mid-1;
        }
    }
    return left;
}