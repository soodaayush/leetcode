// https://leetcode.com/problems/convert-a-number-to-hexadecimal/

// Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s
// complement method is used.

// All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in
// the answer except for the zero itself.

// Note: You are not allowed to use any built-in library method to directly solve this problem.

#include <iostream>
#include <string>

using namespace std;

string toHex(int num) {
    unsigned int aNum = num;

    string hex;
    char array[17] = "0123456789abcdef";

    do {
        hex += array[aNum % 16];
        aNum /= 16;
    } while (aNum);

    return {hex.rbegin(), hex.rend()};
}

int main() {
    toHex(26);
}