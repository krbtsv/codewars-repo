const between = require('./what_is_between')

test('test-ok', () => {
  expect(between(1, 4)).toEqual([1, 2, 3, 4])
  expect(between(-2, 2)).toEqual([-2, -1, 0, 1, 2])
})