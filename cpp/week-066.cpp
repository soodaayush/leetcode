// https://leetcode.com/problems/h-index-ii/

// Given an array of integers citations where citations[i] is the number of citations a researcher
// received for their ith paper and citations is sorted in ascending order, return the researcher's h-index.

// According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of
// h such that the given researcher has published at least h papers that have each been cited at least h times.

// You must write an algorithm that runs in logarithmic time.

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
    vector<int> citations {1, 2, 100};
    hIndex(citations);
}