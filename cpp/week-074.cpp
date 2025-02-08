// https://leetcode.com/problems/climbing-stairs/

// You are climbing a staircase. It takes n steps to reach the top.

// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

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