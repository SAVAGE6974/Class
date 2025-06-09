// function addNumber(){
//     let num1 = 2;
//     let num2 = 3;
//     let sum = num1 + num2;
//     console.log(`결과값: ${sum}`);
// }

// addNumber();
// addNumber();

// var sum = 0;
// function addNumber() {
//     // var result;
//     sum = 10 + 20;
//     result = 10 * 20;
// }

// addNumber();
// console.log(sum);
// console.log(result);

// var x = 10;
// function displayNumber() {
//     console.log(`x is ${x}`);
//     console.log(`y is ${y}`);
//     let y = 20;
// }

// displayNumber();

// var a = 2;
// var a = 5;
// console.log(a);

// let b = 2;
// b = 5;
// console.log(b);

// function multiple(a, b = 5, c = 10) {
//     return a * b + c;
// }

// console.log(multiple(5, 10, 20));
// console.log(multiple(10, 20));
// console.log(multiple(30));

// let sum = function(a, b) {
//     return a + b;
// }

// console.log(`함수 실행결과 : ${sum(10, 20)}`);

// (function(a, b){
//     sum = a + b;
// }(100, 200))

let sum = (a, b) => a + b;

console.log(`함수 실행 괄고 : ${sum(10, 20)}`)