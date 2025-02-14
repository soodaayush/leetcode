// https://leetcode.com/problems/valid-parentheses/

// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.

#include <iostream>
#include <stack>
#include <unordered_map>

using namespace std;

bool isValid(string s) {
    stack<char> stack;
    unordered_map<char, char> closeToOpen = {
        {')', '('},
        {']', '['},
        {'}', '{'}
    };

    for (char c : s) {
        if (closeToOpen.count(c)) {
            if (!stack.empty() && stack.top() == closeToOpen[c]) {
                stack.pop();
            } else {
                return false;
            }
        } else {
            stack.push(c);
        }
    }

    return stack.empty();
}

int main() {
    string characters = "()";
    bool result = isValid(characters);
    cout << result << endl;
}