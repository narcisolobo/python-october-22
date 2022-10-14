/* 
  Missing Value

  You are given an array of length N that contains, in no particular order,
  integers from 0 to N . One integer value is missing.
  
  Quickly determine and return the missing value.
*/

function missingValue(unorderedNums) {
  // your code here
}

const nums1 = [3, 0, 1];
const expected1 = 2;

const nums2 = [3, 0, 1, 2];
const expected2 = null;
// Explanation: nothing is missing

/* 
  Bonus: now the lowest value can now be any integer (including negatives),
  instead of always being 0. 
*/

const nums3 = [2, -4, 0, -3, -2, 1];
const expected3 = -1;

const nums4 = [5, 2, 7, 8, 4, 9, 3];
const expected4 = 6;

/*****************************************************************************/

// below solutions coded to work when min is not always 0

/**
 * - Time: O(n) linear.
 * - Space: O(1) constant.
 */
function missingValue(unorderedNums) {
  if (unorderedNums.length < 1) {
    return null;
  }

  let min = unorderedNums[0];
  let max = unorderedNums[0];
  let sum = 0;
  let expectedSum = 0;

  for (const n of unorderedNums) {
    if (n < min) {
      min = n;
    }
    if (n > max) {
      max = n;
    }
    sum += n;
  }

  for (let i = min; i <= max; i++) {
    expectedSum += i;
  }
  return sum === expectedSum ? null : expectedSum - sum;
}

/**
 * - Time: O(n) linear.
 * - Space: O(n) linear.
 */
function missingValueSeenTable(unorderedNums) {
  if (unorderedNums.length < 1) {
    return null;
  }

  const seen = {};
  let min = unorderedNums[0];
  let max = unorderedNums[0];

  for (let i = 0; i < unorderedNums.length; i++) {
    if (!seen[unorderedNums[i]]) {
      seen[unorderedNums[i]] = true;
    }
    if (unorderedNums[i] < min) {
      min = unorderedNums[i];
    }
    if (unorderedNums[i] > max) {
      max = unorderedNums[i];
    }
  }

  let val = min + 1;

  while (val < max) {
    if (!seen[val]) {
      return val;
    }
    val += 1;
  }
  return null;
}

module.exports = { missingValue, missingValueSeenTable };