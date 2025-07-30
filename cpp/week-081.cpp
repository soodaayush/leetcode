// https://leetcode.com/problems/monotonic-array/

// An array is monotonic if it is either monotone increasing or monotone decreasing.

// An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array
// nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

// Given an integer array nums, return true if the given array is monotonic, or false
// otherwise.

#include <iostream>
#include <vector>

using namespace std;

bool isMonotonic(vector<int>& nums) {
    bool isIncreasing = true;
    bool isDecreasing = true;

    for (int i = 1; i < size(nums); i++) {
        if (!isIncreasing && !isDecreasing) {
            break;
        }

        if (nums[i] < nums[i - 1]) {
            isIncreasing = false;
        }

        if (nums[i] > nums[i - 1]) {
            isDecreasing = false;
        }
    }

    return isIncreasing || isDecreasing;
}

int main() {
    vector<int> nums {1, 2, 2, 3};
    isMonotonic(nums);
}