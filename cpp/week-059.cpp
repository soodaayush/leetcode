// https://leetcode.com/problems/excel-sheet-column-number/

// Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding
// column number.

#include <iostream>
#include <string>

using namespace std;

int titleToNumber(string columnTitle) {
    int result = 0;

    for (char c: columnTitle) {
        result = result * 26 + (c - 'A' + 1);
    }

    return result;
}

int main() {
    titleToNumber("ZY");
}