const greet = require('./hello_world')

test('test-ok', () => {
  expect(greet()).toBe("hello world!")
})
