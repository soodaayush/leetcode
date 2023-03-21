// https://leetcode.com/problems/sqrtx/

/* Given a non-negative integer x, return the square root of x rounded down to the nearest
integer. The returned integer should be non-negative as well. */

// You must not use any built-in exponent function or operator.

// For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

/**
 * @param {number} x
 * @return {number}
 */

var mySqrt = function (x) {
  let root = 0;
  while (root * root <= x) root++;
  return root - 1;
};
