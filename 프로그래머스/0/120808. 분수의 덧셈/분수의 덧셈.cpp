#include <string>
#include <vector>

using namespace std;

// 최소공배수 구하는 함수
int gcd(int a, int b){
    while (b!=0){
        int r = a%b;
        a=b;
        b=r;
    }
    return a;
}

long long lcm(long long a, long long b){
    return a/gcd(a,b)*b;
}

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    vector<int> answer;
    long long denom = denom1 * denom2;
    long long new_numer1 = numer1 * denom2;
    long long new_numer2 = numer2 * denom1;
    long long numer = new_numer1 + new_numer2;
    long long c = gcd(denom, numer);
    answer.push_back(numer/c);
    answer.push_back(denom/c);
    return answer;
}