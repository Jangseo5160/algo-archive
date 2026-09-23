#include <string>
#include <vector>

using namespace std;

bool isPrime(int a){
    if(a<2) return false;
    for (int i=2; i*i<=a; i++){
        if(a%i==0) return false;
    }
    return true;
}

vector<int> solution(int n) {
    vector<int> answer;
    vector<int> temp;

    for(int i=2; i<=n; i++){
        if(n%i==0) temp.push_back(i);
    }
    for(int a:temp){
        if (isPrime(a)) answer.push_back(a);
    }
    return answer;
}