#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    vector<int> nums;
    string temp = "";
    for (char c:s){
        if (c==' '){
            nums.push_back(stoi(temp));
            temp="";
        }
        else{
            temp+=c;
        }
    }
    nums.push_back(stoi(temp));
    int min_val = nums[0];
    int max_val = nums[0];
    for (int num:nums){
        if(num>max_val) max_val = num;
        if(num<min_val) min_val = num;
    }
    return to_string(min_val) + " " + to_string(max_val);
}