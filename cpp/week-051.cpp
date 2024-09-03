// https://leetcode.com/problems/fizz-buzz/

// Given an integer n, return a string array answer (1-indexed) where:
// answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
// answer[i] == "Fizz" if i is divisible by 3.
// answer[i] == "Buzz" if i is divisible by 5.
// answer[i] == i (as a string) if none of the above conditions are true.

#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> fizzBuzz(int n) {
    vector<string> array;

    for (int i = 1; i <= n; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            array.push_back("FizzBuzz");
        } else if (i % 3 == 0) {
            array.push_back("Fizz");
        } else if (i % 5 == 0) {
            array.push_back("Buzz");
        } else {
            array.push_back(to_string(i));
        }
    }

    for(string i: array) {
        cout << i << endl;
    }

    return array;
}

int main() {
    int n = 3;
    fizzBuzz(3);
}