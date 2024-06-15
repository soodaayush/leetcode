// https://leetcode.com/problems/max-consecutive-ones/

// Given a binary array nums, return the maximum number of consecutive 1's in the array.

#include <iostream>
#include <vector>

using namespace std;

int findMaxConsecutiveOnes(vector<int>& nums) {
    int oldConsecutiveCount = 0;
    int newConsecutiveCount = 0;

    for(int i: nums) {
        if (i == 1) {
            newConsecutiveCount += 1;
        }

        if (newConsecutiveCount > oldConsecutiveCount) {
            oldConsecutiveCount = newConsecutiveCount;
        }

        if (i != 1) {
            newConsecutiveCount = 0;
        }
    }

    cout << oldConsecutiveCount << endl;
    return oldConsecutiveCount;
}

int main() {
    vector<int> nums {1, 1, 1, 0, 0, 0, 1};
    findMaxConsecutiveOnes(nums);
}
