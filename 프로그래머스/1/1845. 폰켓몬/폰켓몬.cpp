#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    int len = nums.size();
    unordered_map <int, int> mp;
    for(auto n:nums){
        mp[n]++;
    }
    if(mp.size()<=len/2){
        return mp.size();
    }
    else{
        return len/2;
    }
    return answer;
}