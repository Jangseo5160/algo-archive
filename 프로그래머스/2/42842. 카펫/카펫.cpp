#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
// a, b => a*b = brown + yellow
// a-2 * b-2 = yellow

// a= 가로가 더 큼, b=세로
    int area = brown + yellow;
    for (int width=1; width<=area/2; width++){
        if (area%width==0){
            int height = area/width;
            if( (width-2) * (height-2) == yellow){
                answer = {width, height};
            }
        }

    }
    return answer;
}