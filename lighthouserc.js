module.exports = {
  ci: {
    collect: {
      staticDistDir: './dist/',
      maxAutodiscoverUrls: 1,
      numberOfRuns: 5
    },
    upload: {
      target: 'temporary-public-storage'
    }
  }
}
