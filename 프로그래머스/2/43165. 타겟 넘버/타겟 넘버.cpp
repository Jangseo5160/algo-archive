#include <string>
#include <vector>

using namespace std;

int dfs(vector<int> numbers, int target, int idx, int sum){
    if(idx == numbers.size()){
        if(sum ==target){
           return 1; 
        }
        return 0;
    }
    int count = 0;
    count += dfs(numbers, target, idx+1, sum+numbers[idx]);
    count += dfs(numbers, target, idx+1, sum-numbers[idx]);
    return count;
}


int solution(vector<int> numbers, int target) {
    return dfs(numbers, target, 0,0);
}