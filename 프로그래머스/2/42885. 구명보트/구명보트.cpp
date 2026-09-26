#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(), people.end());
    int left = 0;
    int right = people.size()-1;
    while(left<=right){
        if(left==right){
            answer++;
            break;
        }
        if(people[left]+people[right]<=limit){
            answer++;
            left++;
            right--;
        }
        else{
            answer++;
            right--;
        }
    }
    return answer;
}