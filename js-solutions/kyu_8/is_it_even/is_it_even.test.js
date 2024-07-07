const testEven = require('./is_it_even')

test('test-ok-1', () => {
    expect(testEven(2)).toBe(true)
})

test('test-ok-2', () => {
    expect(testEven(3)).toBe(false)
})