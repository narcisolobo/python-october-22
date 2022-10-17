# Recursion

Recursion is a function that calls itself within its own definition.

```js
function myFunc(){
    myFunc();
}
```

## Base Case - Most important ingredient

It's a way out of the loop. It's like a short circuit.

```js
for(let i = 0; i <= 10; i++) {
    console.log(i);
}
```

## You must progress towards the base case

Think aboud eating a burger

```
func eatBurger() {
    // base case
    if (burger is done) {
        stop eating
    }

    take bite of burger

    eatBurger();
}
```

## We must call the function inside of itself

Call stack - LIFO (Last In First Out)

call p1To255(1)
    log num
    call p1to255(2) - 1st recursive call
        log num
        call p1to255(3) - 1st recursive call

