#include <string>
#include <vector>
#include <unordered_set>
using namespace std;

bool isPrime(int a){
    if(a<2) return false;
    for(int i=2; i*i<=a; i++){
        if(a%i==0) return false;
    }
    return true;
}
unordered_set <int> group;


void dfs(string s, string& numbers, vector<bool> v){
    if(s.size()>0){
        group.insert(stoi(s));
    }
    for(int i=0; i<numbers.size(); i++){
        if(!v[i]){
            v[i]=true;
            dfs(s+numbers[i], numbers, v);
            v[i]=false;
        }
    }
}

int solution(string numbers) {
    int answer = 0;
    vector<bool> v(numbers.size()+1, false);
    dfs("", numbers, v);
    for(auto a: group){
        if(isPrime(a)) answer++;
    }
    return answer;
}