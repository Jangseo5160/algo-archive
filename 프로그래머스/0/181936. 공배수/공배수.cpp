#include <string>
#include <vector>

using namespace std;
int gcd(int a, int b){
    return b ? gcd(b, a%b) : a;
} 
int lcm(int a, int b){
    return a/gcd(a, b)*b;
}

int solution(int number, int n, int m) {
    int answer = 0;
    int temp = lcm(n, m);
    if(number%temp==0) return 1;
    return 0;
}