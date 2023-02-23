const toAlternatingCase = require('./alternating_case')

test('test-ok', () => {
  expect('hello world'.toAlternatingCase()).toBe('HELLO WORLD')
  expect('hEllO world'.toAlternatingCase()).toBe('HeLLo WORLD')
  expect('hello woRld'.toAlternatingCase()).toBe('HELLO WOrLD')
})

test('test-ok-2', () => {
  expect('HeLLo WoRLD'.toAlternatingCase()).toBe('hEllO wOrld')
})