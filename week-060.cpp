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
    cout << result << endl;
    return result;
}

int main() {
    convertToTitle(28);
}