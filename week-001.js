// Given an integer x, return true if x is a palindrome, and false otherwise.

/**
 * @param {number} x
 * @return {boolean}
 */

var isPalindrome = function (x) {
  let string = String(x);
  let reversed = string.split("").reverse().join("");

  if (reversed === string) {
    return true;
  }

  return false;
};
