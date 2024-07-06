function take(arr, num) {
    let firstNumElementsOfArr = [];

    for (let i = 0; i < num && i < arr.length; i++) {
        firstNumElementsOfArr.push(arr[i]);
    }

    return firstNumElementsOfArr;
}

console.log(take([1,2,3,4,5], 3));