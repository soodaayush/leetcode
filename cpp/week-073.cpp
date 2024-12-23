// https://leetcode.com/problems/maximum-average-subarray-i/

// You are given an integer array nums consisting of n elements, and an integer k.

// Find a contiguous subarray whose length is equal to k that has the maximum
// average value and return this value. Any answer with a calculation error less
// than 10-5 will be accepted.

#include <iostream>
#include <vector>

using namespace std;

double findMaxAverage(vector<int>& nums, int k) {
    double currentSum = 0, maxSum = 0;

    for (int i = 0; i < k; i++) {
        currentSum += nums[i];
    }
    maxSum = currentSum;

    for (int i = k; i < nums.size(); i++) {
        currentSum += nums[i] - nums[i - k];
        maxSum = max(maxSum, currentSum);
    }

    return maxSum / k;
}

int main() {
    vector<int> nums {1, 12, -5, -6, 50, 3};
    int k = 4;
    findMaxAverage(nums, k);
}