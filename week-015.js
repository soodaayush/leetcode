// https://leetcode.com/problems/first-unique-character-in-a-string/

/* Given a string s, find the first non-repeating character in it and return its index. If it does
not exist, return -1. */

/**
 * @param {string} s
 * @return {number}
 */

var firstUniqChar = function (s) {
  for (i = 0; i < s.length; i++) {
    if (s.indexOf(s[i]) === s.lastIndexOf(s[i])) return i;
  }

  return -1;
};
