#include <iostream>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    for(auto i=1; i<=n; i++){
        for (int j=0; j<i;j++){
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}