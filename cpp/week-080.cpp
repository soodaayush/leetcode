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