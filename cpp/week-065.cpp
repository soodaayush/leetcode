// https://leetcode.com/problems/single-element-in-a-sorted-array/

// You are given a sorted array consisting of only integers where every element appears exactly
// twice, except for one element which appears exactly once.

// Return the single element that appears only once.

// Your solution must run in O(log n) time and O(1) space.

#include <iostream>
#include <vector>

using namespace std;

int singleNonDuplicate(vector<int>& nums) {
    int left = 0;
    int right = nums.size() - 1;

    while (left < right) {
        int mid = left + (right - left) / 2;

        if (mid % 2 == 1) {
            mid--;
        }

        if (nums[mid] == nums[mid + 1]) {
            left = mid + 2;
        }

        else {
            right = mid;
        }
    }

    cout << nums[left] << endl;
    return nums[left];
}

int main() {
    vector<int> nums {3, 3,7,7,10,11,11};
    singleNonDuplicate(nums);
}