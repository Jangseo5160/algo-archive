#include <string>
#include <vector>

using namespace std;

int gcd(int a, int b){
    return b ? gcd(b, a%b) : a;
}

int lcm(int a, int b){
    return a/gcd(a, b)*b;
}

int solution(int n) {
    int answer = 0;
    answer = lcm(6, n)/6;
    return answer;
}