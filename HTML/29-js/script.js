function calculate(a, b) {
    let result = a + b;
    result = result / 2;
    result = result * 100;
    result = recalculate(result)
    return result;
}


function recalculate(number) {
    let result = number * 0.5;
    result = result - 100;
    // throw 'some error';
    return result;
}