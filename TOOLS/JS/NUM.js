// NUMS






// // MATH LIB

// let a = Math.round(10.5)
// let b = Math.floor(10.3)
// let c = Math.ceil(10.3)
// let d = Math.trunc(10.3)    // премахва след запетаята
// let e = Math.pow(5, 2)      // степенува
// let f = Math.sqrt(81)
// let g = Math.log(2)         // логаритъм
// let h = Math.sin(1)
// let i = Math.cos(1)
// let j = Math.tan(1)
// let k = Math.abs(-10)
// let l = Math.sign(-10)
// let m = Math.min(1, 5,10)

// console.log(d)



// RANDOM

let rand;
const min = 5;
const max = 10;

// randomNum = Math.random()                            // между 0 и 1
// randomNum = Math.floor(Math.random() * 6)            // между 0 и 6
rand = Math.floor(Math.random() * (max - min+1)) + min;  // между 3 и 6
console.log(rand)



// RANDOM COLOR GENERATOR
function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
  

function changeHeaderColor() {
    header.style.color = getRandomColor();
}  

setInterval(changeHeaderColor(), 500)   // в милисекунди




// ДЕСЕТИЧНА ЗАПЕТАЯ
let num = 10; 
console.log(num.toFixed(2))