// https://leetcode.com/problems/excel-sheet-column-title/

// Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string convertToTitle(int columnNumber) {
    string result;

    while (columnNumber > 0) {
        columnNumber--;
        int remainder = columnNumber % 26;
        result += (remainder + 'A');
        columnNumber /= 26;
    }

    reverse(result.begin(), result.end());
    return result;
}

int main() {
    convertToTitle(28);
}