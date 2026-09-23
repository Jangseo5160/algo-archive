#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

int solution(vector<int> array, int n) {
    int answer = array[0];
    
    for(int a:array){
        int dist = abs(a-n);
        int min_dist = abs(answer-n);
        if(dist<min_dist){
            answer=a;
        }
        else if(dist==min_dist && a<answer){
            answer=a;
        }
    }
    
    return answer;
}