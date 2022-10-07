/* 
  Given an array of objects to represent new inventory
  and an array of objects to represent current inventory,
  update the quantities of the current inventory
  
  if the item doesn't exist in current inventory,
  add it to the current inventory

  return the current inventory after updating it.
*/

const newInv1 = [
  { name: "Grain of Rice", quantity: 9000 },
  { name: "Peanut Butter", quantity: 50 },
  { name: "Royal Jelly", quantity: 20 },
];
const currInv1 = [
  { name: "Peanut Butter", quantity: 20 },
  { name: "Grain of Rice", quantity: 1 },
];
const expected1 = [
  { name: "Peanut Butter", quantity: 70 },
  { name: "Grain of Rice", quantity: 9001 },
  { name: "Royal Jelly", quantity: 20 },
];

const newInv2 = [];
const currInv2 = [{ name: "Peanut Butter", quantity: 20 }];
const expected2 = [{ name: "Peanut Butter", quantity: 20 }];

const newInv3 = [{ name: "Peanut Butter", quantity: 20 }];
const currInv3 = [];
const expected3 = [{ name: "Peanut Butter", quantity: 20 }];

function updateInventory(newInv, currInv) {
  
  // outer for loop for newInv
  for (let i = 0; i < newInv.length; i++) {
    // set boolean flag to show if the newInv item
    // exists in the currInv
    let isPresent = false;
    
    // inner loop for currInv
    for (let j = 0; j < currInv.length; j++) {
      // check each item in currInv for matching name
      if (newInv[i].name === currInv[j].name) {
        // set flag to true if I find a match
        isPresent = true;
        // also update currInv quantity
        currInv[j].quantity += newInv[i].quantity;
      }
    }

    // if I did not find item in currInv, push to currInv
    if (!isPresent) {
      currInv.push(newInv[i]);
    }

  }
  return currInv;
}

result = updateInventory(newInv1, currInv1);
console.log(result);