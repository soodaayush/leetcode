// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

// You are given an array prices where prices[i] is the price of a given stock on the ith day.
// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#include <iostream>
#include <vector>

using namespace std;

int maxProfit(vector<int>& prices) {
    int buyPrice = prices[0];
    int profit = 0;

    for (int i = 1; i < prices.size(); i++) {
        if (buyPrice > prices[i]) {
            buyPrice = prices[i];
        }

        profit = max(profit, prices[i] - buyPrice);
    }

    cout << profit << endl;
    return profit;
}

int main() {
    vector<int> prices {1, 2, 5, 6, 3, 5};
    maxProfit(prices);
}