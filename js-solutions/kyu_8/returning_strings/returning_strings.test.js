const greet = require('./returning_strings')

test('test-ok-1', () => {
    expect(greet('Max')).toBe('Hello, Max how are you doing today?')
})

test('test-ok-2', () => {
    expect(greet('Shingles')).toBe('Hello, Shingles how are you doing today?')
})
