#include <string>
#include <vector>

using namespace std;

int solution(vector<int> people, int limit) {
    vector<int> cnt(241, 0);
    for(int x: people){
        cnt[x]++;
    }
    int left =0;
    int right=240;
    int answer=0;
    
    while (left<=right){
        while(left<=right && cnt[left]==0){
            left++;
        }
        while (left<=right && cnt[right]==0){
            right--;
        }
        if(left>right){
            break;
        }
        cnt[right]--;
        answer++;
        if(left<=right && left+right<=limit && cnt[left]>0){
            cnt[left]--;
        }
        
    }
    return answer;
}