#include <string>
#include <vector>

using namespace std;
int gcd(int a, int b){
    return b ? gcd(b, a%b) : a;
}
int lcm(int a, int b){
    return a/gcd(a, b) *b;
}
int solution(vector<int> arr) {
    int answer = 0;
    int a=arr[0];
    for(int i=1; i<arr.size(); i++){
        a= lcm(a, arr[i]);
    }
    return a;
}