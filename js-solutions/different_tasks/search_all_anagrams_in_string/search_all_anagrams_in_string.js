function searchAllAnagramsInString(str, substr) {
    const result = [];
    const subStrLength = substr.length;
    const sortedSubStr = substr.split('').sort().join('');

    for (let i = 0; i <= str.length; i++) {
        if (str.substring(i, i + subStrLength).split('').sort().join('') === sortedSubStr) {
            result.push(i)
        }
    }

    return result;
}

module.exports = searchAllAnagramsInString;