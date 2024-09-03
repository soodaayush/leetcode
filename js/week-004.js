// https://leetcode.com/problems/roman-to-integer/

/* Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. */

/* For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII,
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II. */

/* Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is 
not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is 
used: */

/* Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is 
not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is 
used: */

// I can be placed before V (5) and X (10) to make 4 and 9.

// X can be placed before L (50) and C (100) to make 40 and 90.

// C can be placed before D (500) and M (1000) to make 400 and 900.

// Given a roman numeral, convert it to an integer.

/**
 * @param {string} s
 * @return {number}
 */

var romanToInt = function (s) {
  let I = 1;
  let V = 5;
  let X = 10;
  let L = 50;
  let C = 100;
  let D = 500;
  let M = 1000;

  s = s.split("");

  let value = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "I") {
      if (s[i + 1] === "V") {
        value = value + V - I;
      }

      if (s[i + 1] === "X") {
        value = value + X - I;
      }

      if (s[i + 1] !== "V" && s[i + 1] !== "X") {
        value = value + I;
      }
    }

    if (s[i] === "V") {
      if (i >= 0) {
        if (s[i - 1] !== "I") {
          value = value + V;
        }
      }
    }

    if (s[i] === "L") {
      if (i >= 0) {
        if (s[i - 1] !== "X") {
          value = value + L;
        }
      }
    }

    if (s[i] === "C") {
      if (s[i + 1] === "D") {
        value = value + D - C;
      }

      if (s[i + 1] === "M") {
        value = value + M - C;
      }

      if (s[i + 1] !== "D" && s[i + 1] !== "M" && s[i - 1] !== "X") {
        value = value + C;
      }
    }

    if (s[i] === "D") {
      if (i >= 0) {
        if (s[i - 1] !== "C") {
          value = value + D;
        }
      }
    }

    if (s[i] === "M") {
      if (i >= 0) {
        if (s[i - 1] !== "C") {
          value = value + M;
        }
      }
    }

    if (s[i] === "X") {
      if (s[i + 1] === "L") {
        value = value + L - X;
      }

      if (s[i + 1] === "C") {
        value = value + C - X;
      }

      if (s[i + 1] !== "L" && s[i + 1] !== "C" && s[i - 1] !== "I") {
        value = value + X;
      }
    }
  }

  return value;
};
