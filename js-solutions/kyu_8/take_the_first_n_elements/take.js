function take(arr, num) {
    let firstNumElementsOfArr = [];

    for (let i = 0; i < num && i < arr.length; i++) {
        firstNumElementsOfArr.push(arr[i]);
    }

    return firstNumElementsOfArr;
}

module.exports = take;