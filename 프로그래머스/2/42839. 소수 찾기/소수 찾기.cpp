#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;
bool isPrime(int n) {
    if (n < 2)
        return false;

    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }

    return true;
}
int solution(string numbers) {
    int answer = 0;
    set<int> nums;
    vector<int> order;
    sort(numbers.begin(), numbers.end());
    do{
        int num=0;
        for(char c:numbers){
            num = num*10 + (c-'0');
            nums.insert(num);
        }
        
    }while(next_permutation(numbers.begin(), numbers.end()));
    
    for(auto n:nums){
        if(isPrime(n)) answer++;
    }
    
    return answer;
}