/* 
Write a recursive that prints a count down to 0 from a given number.
*/


function countDown(num) {
  if (num == -1) {
    return;
  }

  console.log(num);
  num--;

  countDown(num);
}

// countDown(10);

/* 
Print all the integers from 1 to 255.
*/

function print1To255(num = 1) {
  if (num == 3) {
    return;
  };

  console.log(num);

  print1To255(num + 1);
}

print1To255();