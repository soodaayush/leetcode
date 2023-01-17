// https://leetcode.com/problems/length-of-last-word/description/

// Given a string s consisting of words and spaces, return the length of the last word in the string.

// A word is a maximal substring consisting of non-space characters only.

/**
 * @param {string} s
 * @return {number}
 */

var lengthOfLastWord = function (s) {
  s = s.split(" ");

  s = s.filter((word) => word !== "");

  let index = s.length - 1;

  return s[index].length;
};
