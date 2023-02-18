const getAge = require('./parse_int')

test('test-ok', () => {
    expect(getAge("5 ears old")).toBe(5)
})