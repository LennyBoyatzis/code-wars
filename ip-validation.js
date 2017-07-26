const expect = require('chai').expect

function isValidIP(str) {
  return str.split('.')
    .filter(section => parseInt(section) <= 256)
    .length === 4
}

describe('isValidIP', () => {
  it('returns valid when the address has 4 sections split by decimals', () => {
    const result = isValidIP('123.45.67.89')
    expect(result).to.equal(true)
  })

  it('return invalid when the address doesnt have 4 sections split by decimals', () => {
    const result = isValidIP('123.45.67.89.98')
    expect(result).to.equal(false)
  })

  it('returns true when all of the individual sections are less than or equal to 256', () => {
    const result = isValidIP('123.45.123.89')
    expect(result).to.equal(true)
  })

  it('returns false when all of the individual sections are less than or equal to 256', () => {
    const result = isValidIP('123.45.257.89')
    expect(result).to.equal(false)
  })
})

