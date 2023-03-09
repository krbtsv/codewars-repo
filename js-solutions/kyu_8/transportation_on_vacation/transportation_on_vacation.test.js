const rentalCarCost = require('./transportation_on_vacation')


test('test-ok-1', () => {
    expect(rentalCarCost(2)).toBe(80)
})

test('test-ok-2', () => {
    expect(rentalCarCost(3)).toBe(100)
})

test('test-ok-3', () => {
    expect(rentalCarCost(7)).toBe(230)
})

test('test-ok-2', () => {
    expect(rentalCarCost(10)).toBe(350)
})
