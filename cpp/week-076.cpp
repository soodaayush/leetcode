// https://leetcode.com/problems/number-of-1-bits/

// Given a positive integer n, write a function that returns the number of set bits
// in its binary representation (also known as the Hamming weight).

#include <iostream>
#include <cstdint>

using namespace std;

int hammingWeight(uint32_t n) {
    int res = 0;

    for (int i = 0; i < 32; i++) {
        if ((1 << i) & n) {
            res++;
        }
    }

    return res;
}

int main() {
    int n = 00000000000000000000000000010111;
    int result = hammingWeight(n);
    cout << result << endl;
}