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