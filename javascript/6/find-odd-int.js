const path = require('path')
const filename = path.basename(__filename)

/* Find the Odd Int
 *
 * Given an array of integers, find the one that appears an odd number of times.
 *
 * There will always be only one integer that appears an odd number of times.
 *
 * Examples:
 *   [7] should return 7, because it occurs 1 time (which is odd).
 *   [0] should return 0, because it occurs 1 time (which is odd).
 *   [1,1,2] should return 2, because it occurs 1 time (which is odd).
 *   [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
 *   [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
 */

function findOdd(ints) {
  if (ints.length === 1) return ints[0]

  const dict = {}
  for (let i of ints) {
    if (dict[i]) {
      dict[i]++
    } else {
      dict[i] = 1
    }
  }

  for (const [key, value] of Object.entries(dict)) {
    if (value % 2 !== 0) {
      return Number(key)
    }
  }
}

// Uses ternary
function findOdd2(ints) {
  const dict = {}

  for (let i of ints) {
    dict[i] ? dict[i]++ : (dict[i] = 1)
  }

  for (const [key, value] of Object.entries(dict)) {
    if (value % 2 !== 0) {
      return Number(key)
    }
  }
}

console.log(`Running: ${filename}`)
console.log(findOdd([7]))
console.log(findOdd([1, 1, 2]))
console.log(findOdd([1, 2, 2, 3, 3, 3, 4, 3, 3, 2, 2, 1]))
console.log(findOdd([0, 1, 0, 1, 0]))
console.log('-----')
console.log(findOdd2([7]))
console.log(findOdd2([1, 1, 2]))
console.log(findOdd2([1, 2, 2, 3, 3, 3, 4, 3, 3, 2, 2, 1]))
console.log(findOdd2([0, 1, 0, 1, 0]))
