#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    for (int num=1; num<=n; num++){
        int temp_cnt=0;
        for (int i=1; i<=num; i++){
            if (num%i==0){
                temp_cnt ++;
            }
        }
        if(temp_cnt>2) answer++;
    }
    return answer;
}