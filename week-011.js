// https://leetcode.com/problems/add-to-array-form-of-integer/

// The array-form of an integer num is an array representing its digits in left to right order.

// For example, for num = 1321, the array form is [1,3,2,1].

/* Given num, the array-form of an integer, and an integer k, return the array-form of the
integer num + k. */

/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function (num, k) {
  num = num.join("");

  num = BigInt(num);

  k = BigInt(k);

  num = num + k;

  num = Array.from(String(num), Number);

  return num;
};
