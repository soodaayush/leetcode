// https://leetcode.com/problems/valid-palindrome/

/* A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers. */

// Given a string s, return true if it is a palindrome, or false otherwise.

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  s = s.replaceAll(" ", "").toLowerCase();

  s = s.replaceAll(/[^a-zA-Z0-9 ]/g, "");

  if (s.split("").reverse().join("") === s) {
    return true;
  }

  return false;
};
