// https://leetcode.com/problems/rotate-array/

// Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

#include <iostream>
#include <vector>

using namespace std;

void rotate(vector<int>& nums, int k) {
    if (k == 0) return;

    int n = nums.size();
    k = k % n;
    vector<int> rotated(n);

    for (int i = 0; i < n; i++) {
        rotated[(i + k) % n] = nums[i];
    }

    for (int i = 0; i < n; i++) {
        nums[i] = rotated[i];
    }
}