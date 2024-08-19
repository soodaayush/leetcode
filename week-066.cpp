// https://leetcode.com/problems/single-element-in-a-sorted-array/

// You are given a sorted array consisting of only integers where every element appears exactly
// twice, except for one element which appears exactly once.

// Return the single element that appears only once.

// Your solution must run in O(log n) time and O(1) space.

#include <iostream>
#include <vector>

using namespace std;

int hIndex(vector<int>& citations) {
    int size = citations.size();
    int left = 0;
    int right = size - 1;
    int citationCount = 0;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (citations[mid] >= size - mid) {
            citationCount = size - mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    cout << citationCount << endl;
}

int main() {
    vector<int> nums {1, 2, 100};
    hIndex(nums);
}