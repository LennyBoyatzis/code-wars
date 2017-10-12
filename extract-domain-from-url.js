const { expect } = require('chai');

function domainName(url) {
  return url
    .replace(/http:\/\//, '')
    .replace(/https:\/\//, '')
    .replace(/www./, '')
    .split('.')[0]
}

describe('domainName', () => {
  it('http://google.com.au', () => {
    expect(domainName('http://google.com.au')).to.equal('google')
  });

  it('http://google.co.jp', () => {
    expect(domainName('http://google.co.jp')).to.equal('google')
  });

  it('www.xakep.ru', () => {
    expect(domainName('www.xakep.ru')).to.equal('xakep')
  });

  it('https://youtube.com', () => {
    expect(domainName('https://youtube.com')).to.equal('youtube')
  });
});
