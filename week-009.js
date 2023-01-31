// https://leetcode.com/problems/powx-n/

// Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */

var myPow = function (x, n) {
  let answer = 0;

  if (n === 1) {
    return x;
  }

  if (n === 0) {
    return 1;
  }

  if (x === -1 && Math.sign(n) === -1) {
    if (n % 2 === 0) {
      return 1;
    } else {
      return -1;
    }
  }

  if (n > 0) {
    for (let i = 0; i < n; i++) {
      answer = x ** n;
    }
  }

  if (n < 0) {
    n = n * -1;

    for (let i = 0; i < n; i++) {
      answer = x ** n;
    }

    answer = 1 / answer;
  }

  return answer;
};
