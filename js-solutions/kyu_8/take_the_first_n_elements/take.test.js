const take = require('./take');

test('test-ok', () => {
    expect(take([0, 1, 2, 2, 2, 1], 2)).toEqual([0, 1])
})