// https://leetcode.com/problems/reverse-integer/

/* Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to
go outside the signed 32-bit integer range [-231, 231 - 1], then return 0. */

// Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

/**
 * @param {number} x
 * @return {number}
 */

var reverse = function (x) {
  x = x.toString();

  x = x.split("");

  x = x.reverse();

  if (x[x.length - 1] === "-") {
    x.pop();
    x.unshift("-");
  }

  x = x.join("");

  if (x >= Math.pow(2, 31) - 1 || x <= Math.pow(-2, 31)) {
    return 0;
  }

  x = parseFloat(x);

  return x;
};
