#include <string>
#include <vector>

using namespace std;

int solution(string name) {
    int answer = 0;
    for(auto a:name){
        answer += min(a - 'A', 'Z'-a+1);
    }
    int n= name.size();
    int dist = n-1;
    for(int i=0; i<n; i++){
        int j=i+1;
        if(name[j]=='A'){
            while(name[j]=='A')
                j++;
        }
        int left_back = i*2 + n-j;
        int right_back = (n-j)*2 + i;
        dist = min(min(left_back,right_back), dist);
    }
    answer+=dist;
    return answer;
}