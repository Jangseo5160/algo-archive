#include <string>
#include <vector>
#include <set>

using namespace std;
int answer = 0;
vector <bool> visited;
set<int> every_nums;

bool isPrime(int a){
    if(a<2) return false;
    for(int i=2; i*i<=a; i++){
        if(a%i==0) return false;
    }
    return true;
}

void dfs(string& numbers, string num){
    if(!num.empty()){
        every_nums.insert(stoi(num));
    }
    
    for(int i=0; i<numbers.size(); i++){
        if(!visited[i]){
            visited[i]=true;
            dfs(numbers, num+numbers[i]);
            visited[i]=false;
        }
        
    }
}

int solution(string numbers) {
    int answer = 0;
    visited.assign(numbers.size(), false);

    dfs(numbers, "");
    
    for(int n:every_nums){
        if (isPrime(n)){
            answer++;
        }
    }
    
    return answer;
}