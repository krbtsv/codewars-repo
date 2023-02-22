const countBy = require('./count_by_x')

test('test-ok', () => {
  expect(countBy(1, 10)).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
})
