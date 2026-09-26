#include <string>
#include <vector>
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    long long answer = 0;
    long long left = 0;
    long long right = distance;
    
    rocks.push_back(distance);
    sort(rocks.begin(), rocks.end());
    
    while(left<=right){
        long long mid = (left+right)/2;
        long long cnt=0;
        long long prev = 0;
        
        for(int i=0; i<rocks.size(); i++){
            if((rocks[i]-prev)<mid){
                cnt++;
            }
            else{
                prev = rocks[i];
            }
        }
        if(cnt<=n){
            left=mid+1;

        }
        else{
            right=mid-1;
        }
    }
    return right;
}