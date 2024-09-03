// https://leetcode.com/problems/add-binary/

// Given two binary strings a and b, return their sum as a binary string.

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string a = "11";
    string b = "1";

    int lengthDifference;
    char stringToLengthen;

    if (a.length() != b.length()) {
       if (a.length() > b.length()) {
           lengthDifference = a.length() - b.length();
           stringToLengthen = 'B';
       }

        if (b.length() > a.length()) {
            lengthDifference = b.length() - a.length();
            stringToLengthen = 'A';
        }
    }

    cout << "Original String #1: " << a << endl;
    cout << "Original String #2: " << b << endl;

    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    int lengths = max(a.length(), b.length());

    cout << a << endl;
    cout << b << endl;

    vector<char> aVector;
    vector<char> bVector;
    vector<char> resultVector;

    int carry = 0;

    for (int i = 0; i < a.length(); i++) {
        aVector.push_back(a[i]);
    }

    if (stringToLengthen == 'A') {
        for (int j = 0; j < lengthDifference; j++) {
            aVector.push_back('0');
        }
    }

    for (int i = 0; i < b.length(); i++) {
        bVector.push_back(b[i]);
    }

    if (stringToLengthen == 'B') {
        for (int j = 0; j < lengthDifference; j++) {
            bVector.push_back('0');
        }
    }

    for (int i = 0; i < lengths; i++) {
        if (aVector[i] == '0' && bVector[i] == '0') {
            if (carry == 0) {
                resultVector.push_back('0');
            } else {
                resultVector.push_back('1');
                carry = 0;
            }
        }
        if (aVector[i] == '1' && bVector[i] == '0' || (aVector[i] == '0' && bVector[i] == '1')) {
            if (carry == 0) {
                resultVector.push_back('1');
            } else {
                resultVector.push_back('0');
                carry = 1;
            }
        }
        if (aVector[i] == '1' && bVector[i] == '1') {
            if (carry == 0) {
                resultVector.push_back('0');
                carry = 1;
            } else {
                resultVector.push_back('1');
                carry = 1;
            }
        }

        if (i == (lengths - 1)) {
            if (carry == 1) {
                resultVector.push_back('1');
            }
        }
    }

    reverse(resultVector.begin(), resultVector.end());

    string result(resultVector.begin(), resultVector.end());

    cout << result << endl;
}