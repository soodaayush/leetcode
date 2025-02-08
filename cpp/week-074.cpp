#include <iostream>

using namespace std;

int climbStairs(int n) {
    if (n <= 3) return n;

    int first = 3;
    int second = 2;
    int current = 0;

    for (int i = 3; i < n; i++) {
        current = first + second;
        second = first;
        first = current;
    }

    return current;
}

int main() {
    int n = 2;
    int result = climbStairs(n);
    cout << result << endl;
}