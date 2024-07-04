const searchAllAnagramsInString = require('./search_all_anagrams_in_string')

test('test-ok', () => {
    expect(searchAllAnagramsInString('cbacbebabacd', 'abc')).toEqual([0, 1, 2, 8])
})
