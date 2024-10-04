function try_50(num1=0, num2=0){
    return (num1 === 50) || (num2 === 50) || (num1 + num2 === 50)
}

// console.log(try_50(50, 50));
// console.log(try_50(20, 30));
// console.log(try_50(40, 30));

function try_20(num=0){
    return (Math.abs(100 - num) <= 20) || (Math.abs(400 - num) <= 20)
}

// console.log(try_20(80));
// console.log(try_20(40));
// console.log(try_20(90));
// console.log(try_20(420));


function check_sign(num1=0, num2=0){
    return (num1 < 0 && num2 > 0) || (num1 > 0 && num2 < 0)
}

// console.log(check_sign(-1, 1))
// console.log(check_sign(1, 1))
// console.log(check_sign(1, -1))
// console.log(check_sign(-1, -1))

function check_3_and_7_multiples(num){
    return (num % 3 === 0 || num % 7 === 0) ? true : false;
}

// console.log(check_3_and_7_multiples(8));
// console.log(check_3_and_7_multiples(7));
// console.log(check_3_and_7_multiples(9));


const check_range_50_to_99 = function(num1, num2){
    // return (num1 >= 50 && num1 <= 99) || (num2 >= 50 && num2 <= 99) ? true : false;
    return (num1 >= 50 && num1 <= 99) || (num2 >= 50 && num2 <= 99) ? true : false;
}


console.log(check_range_50_to_99(55, 100));
console.log(check_range_50_to_99(40, 90));
console.log(check_range_50_to_99(55, 90));
console.log(check_range_50_to_99(40, 100));