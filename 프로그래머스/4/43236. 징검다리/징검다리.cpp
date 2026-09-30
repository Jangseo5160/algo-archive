#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    int answer = 0;
    rocks.push_back(distance);
    rocks.push_back(0);
    sort(rocks.begin(), rocks.end());
    int right = distance;
    int left = 0;
    while(left<=right){
        int mid = (left+right)/2;
        int cnt=0;
        int prev=0;
        
        for(int i=1; i<rocks.size(); i++){
            int cur = rocks[i];
            if(cur-prev<mid){
                cnt++;
            }
            else{
                prev=cur;
            }
        }
        if(cnt<=n){
            left=mid+1;
        }
        else{
            right=mid-1;
        }
    }
    answer=right;
    return answer;
}