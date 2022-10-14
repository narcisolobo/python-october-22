/* 
  Array: Mode
  
  Create a function that, given an array
  of ints, returns an array containing
  the int or ints that occur most frequently in the array.

  If there are multiple items that
  occur the same number of time, return
  all of them in an array. Order doesn't
  matter.
  
  If all items occur the same number of
  times return empty array.

*/

function mode(nums) {
  if (nums.length == 0) return [];
  const freqTable = {}
  const modeArr = []
  for (const i in nums) {
    if (freqTable.hasOwnProperty(nums[i])){
      freqTable[nums[i]]++
    } else {
      freqTable[nums[i]] = 1
    }
  }
  console.log(freqTable)
  let max = 0;
  for (const [key, value] of Object.entries(freqTable)) {
    console.log(key, value)
    if (value > max) {
      max = value
    }
  }

  for (const [key, value] of Object.entries(freqTable)) {
    if (value == max) {
      modeArr.push(parseInt(key))
    }
  }
  console.log(modeArr)
}

const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1];
const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
const expected5 = [5, 1];

mode(nums1)
/*****************************************************************************/

/**
 * - Time: O(2n) -> O(n) linear.
 * - Space: O(n) linear.
 */
// function mode(nums) {
//   if (nums.length === 1) {
//     return [nums[0]];
//   }

//   const modes = [];
//   const freq = {};
//   let maxFreq = 0;
//   let allSameFreq = true;

//   for (const n of nums) {
//     freq.hasOwnProperty(n) ? freq[n]++ : (freq[n] = 1);

//     if (freq[n] > maxFreq) {
//       maxFreq = freq[n];
//     }
//   }

//   for (const key in freq) {
//     if (freq[key] === maxFreq) {
//       // Keys are strings, convert back to int. Can be avoided if using a Map.
//       modes.push(parseInt(key));
//     } else {
//       allSameFreq = false;
//     }
//   }
//   // return empty array if allSameFreq, else return modes
//   return allSameFreq ? [] : modes;
// }

// module.exports = { mode };