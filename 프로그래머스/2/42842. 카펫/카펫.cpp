#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int area = brown + yellow;
    for(int h=3; h*h<=area; h++){
        if(area%h==0){
            int w=area/h;
            if((w-2)*(h-2)==yellow){
                answer = {w, h};
                break;
            }
        }
    }
    return answer;
}