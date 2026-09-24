#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    vector<int> total_min;
    vector<int> total_max;
    for(auto a:sizes){
        int min=a[0];
        int max=a[1];
        if(min>max) {
            min=max;
            max=a[0];
        }
        total_min.push_back(min);
        total_max.push_back(max);
    }
    int total = *max_element(total_min.begin(), total_min.end());
    total *= *max_element(total_max.begin(), total_max.end());
    
    return total;
}