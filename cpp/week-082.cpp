// https://leetcode.com/problems/find-the-difference-of-two-arrays/

// Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

// answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
// answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

// Note that the integers in the lists may be returned in any order.

#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
    set<int> set1(nums1.begin(), nums1.end());
    set<int> set2(nums2.begin(), nums2.end());

    vector<int> distinctNums1, distinctNums2;

    for (int i : set1) {
        if (!set2.contains(i)) {
            distinctNums1.push_back(i);
        }
    }

    for (int i : set2) {
        if (!set1.contains(i)) {
            distinctNums2.push_back(i);
        }
    }

    return {distinctNums1, distinctNums2};
}

int main() {
    vector<int> nums1 {1, 2, 3, 3};
    vector<int> nums2 {1, 1, 2, 2};

    findDifference(nums1, nums2);
}