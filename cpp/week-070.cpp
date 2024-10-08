// https://leetcode.com/problems/ransom-note/

// Given two strings ransomNote and magazine, return true if ransomNote
// can be constructed by using the letters from magazine and false otherwise.

// Each letter in magazine can only be used once in ransomNote.

#include <iostream>
#include <unordered_map>

using namespace std;

bool canConstruct(string ransomNote, string magazine) {
    unordered_map<char, int> letterCount;

    for (int i = 0; i < magazine.length(); i++) {
        letterCount[magazine[i]]++;
    }

    for (int i = 0; i < ransomNote.length(); i++) {
        letterCount[ransomNote[i]]--;
        if (letterCount[ransomNote[i]] < 0) {
            return false;
        }
    }

    return true;
}

int main() {
    string ransomNote = "a";
    string magazine = "b";
    canConstruct(ransomNote, magazine);
}