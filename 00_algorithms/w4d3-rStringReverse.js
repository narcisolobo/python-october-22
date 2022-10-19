/* 
  Recursively reverse a string
  helpful methods:

  str.slice(beginIndex, endIndex)
  returns a new string from beginIndex to endIndex exclusive
*/

const str1 = "abc";
const expected1 = "cba";

const str2 = "";
const expected2 = "";


function rStringReverse(str = '') {
  if (str === "") {
    return "";
  }
  const strWithoutFirstChar = str.slice(1);
  const firstChar = str[0];
  return rStringReverse(strWithoutFirstChar) + firstChar;
}

const result = rStringReverse('abc')
console.log(result);