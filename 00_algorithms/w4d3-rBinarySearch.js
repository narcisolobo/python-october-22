/*
  Recursive Binary Search

  Input: SORTED array of ints, int value
  Output: bool representing if value is found

  Recursively search to find if the value exists, do not loop over every element.

  Approach:
  Take the middle item and compare it to the given value.
  Based on that comparison, narrow your search to a particular section of the array
*/

// non-recursive solution
function binarySearch(sortedNums, searchNum) {
  let leftIdx = 0;
  let rightIdx = sortedNums.length - 1;
  while (leftIdx <= rightIdx) {
    let midIdx = Math.floor(rightIdx - leftIdx / 2);
    if (sortedNums[midIdx] === searchNum) {
      return true;
    }
    if (searchNum < sortedNums[midIdx]) {
      rightIdx = midIdx - 1;
    } else {
      leftIdx = midIdx + 1;
    }
  }
  return false;
}

function rBinarySearch(
  sortedNums = [],
  searchNum,
  leftIdx = 0,
  rightIdx = sortedNums.length - 1
) {
  // base case
  if (leftIdx > rightIdx) {
    return false
  };

  // find middle index
  const midIdx = Math.floor((leftIdx + rightIdx) / 2);

  // is item at middle index our searchNum?
  if (searchNum === sortedNums[midIdx]) {
    return true
  };

  // if not, call func again with new arguments
  if (searchNum < sortedNums[midIdx]) {

    // recursive call progresses to base case
    return rBinarySearch(sortedNums, searchNum, leftIdx, midIdx - 1);
  } else {

    // recursive call progresses to base case
    return rBinarySearch(sortedNums, searchNum, midIdx + 1, rightIdx)
  }
}

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

const result1 = rBinarySearch(nums1, searchNum1);
console.log(result1);
const result2 = rBinarySearch(nums2, searchNum2);
console.log(result2);
const result3 = rBinarySearch(nums3, searchNum3);
console.log(result3);