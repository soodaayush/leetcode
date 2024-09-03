// https://leetcode.com/problems/single-number/

/* Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one. */

/* You must implement a solution with a linear runtime complexity and use only constant extra
space. */

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  if (nums.length === 1) {
    return nums[0];
  }

  let set = new Set(nums);

  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] === nums[j]) {
        set.delete(nums[i]);
      }
    }
  }

  return set.values().next().value;
};
