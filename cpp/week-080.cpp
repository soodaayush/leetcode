// https://leetcode.com/problems/find-the-highest-altitude/

// There is a biker going on a road trip. The road trip consists of n + 1 points
// at different altitudes. The biker starts his trip on point 0 with altitude equal
// 0.

// You are given an integer array gain of length n where gain[i] is the net gain in
// altitude between points i and i + 1 for all (0 <= i < n). Return the highest altitude
// of a point.

#include <iostream>
#include <vector>

using namespace std;

int largestAltitude(vector<int>& gain) {
    int currentAltitude = 0;

    int highestPoint = currentAltitude;

    for (int altitudeGain: gain) {
        currentAltitude += altitudeGain;

        highestPoint = max(highestPoint, currentAltitude);
    }

    return highestPoint;
}

int main() {
    vector<int> gain {-5, 1, 5, 0, -7};
    largestAltitude(gain);
}