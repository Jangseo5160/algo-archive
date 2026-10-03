#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    int answer = 0;
    int left=0;
    int right=distance;
    
    rocks.push_back(0);
    rocks.push_back(distance);
    sort(rocks.begin(), rocks.end());
    //0,2,11,14,17,21,25
    while(left<=right){
        int mid=(left+right)/2; //12
        int cnt=0;
        int prev=0;
        for(int i=1; i<rocks.size(); i++){
            if(rocks[i]-rocks[prev]<mid){ //5
                cnt++;
            }
            else{
                prev=i;//14
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