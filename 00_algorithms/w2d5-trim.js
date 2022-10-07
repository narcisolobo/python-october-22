/* 
  Given a string that may have extra spaces at
  the start and the end, return a new string that
  has the extra spaces at the start and the end
  trimmed (removed).

  Do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

function trim(str) {
  // string to eventually return
  let trimmed = "";
  // vars for first and last non-space indexes
  let firstCharIdx;
  let lastCharIdx;

  // start at beginning of string and look
  // for first non-space character's index
  for (var i = 0; i < str.length; i++) {
    if (str[i] !== " ") {
      // if non-space, set firstCharIdx and break
      firstCharIdx = i;
      break;
    }
  }
  
  // start at end of string and look
  // for last non-space character's index
  for (var j = str.length - 1; j >= 0; j--) {
    if (str[j] !== " ") {
      // if non-space, set lastCharIdx and break
      lastCharIdx = j;
      break;
    }
  }

  // start new loop at first non-space index
  // end at last non-space index
  for (let k = firstCharIdx; k <= lastCharIdx; k++) {
    // add characters
    trimmed += str[k];
  }

  return trimmed;
}

result = trim(str1);
console.log(`trimmed: ${result}, length: ${result.length}`);