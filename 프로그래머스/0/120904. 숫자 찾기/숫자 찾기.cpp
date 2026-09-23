#include <string>
#include <vector>

using namespace std;

int solution(int num, int k) {
    int answer = -1;
    int temp_i = to_string(num).size();
    while (num>0){
        int n = num%10;
        num/=10;
        if (n==k){
            answer = temp_i;
        };
        temp_i--;
    }
    return answer;
}