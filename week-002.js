/* Given an array of integers nums which is sorted in ascending order, and an integer target, write a
function to search target in nums. If target exists, then return its index. Otherwise, return -1. */

// You must write an algorithm with O(log n) runtime complexity.

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

var search = function (nums, target) {
  let lo = 0;
  let hi = nums.length - 1;

  if (nums.length === 1 && nums[0] === target) {
    return 0;
  }

  while (lo <= hi) {
    let mid = lo + Math.floor((hi - lo + 1) / 2);

    if (nums[mid] === target) {
      return mid;
    }

    if (nums[mid] > target) {
      hi = mid - 1;
    }

    if (nums[mid] < target) {
      lo = mid + 1;
    }
  }

  return -1;
};
