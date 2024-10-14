/* Find the Parity Outlier
 *
 * You are given an array (which will have a length of at least 3, but could be very large) containing integers.
 * The array is either entirely comprised of odd integers or entirely comprised of even integers except for a
 * single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
 *
 * Examples:
 * [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)
 *
 * [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)
 */

const path = require('path')
const filename = path.basename(__filename)

function findOutlier(integers) {
  let outlier = false

  const first = integers[0] % 2 === 0
  const second = integers[1] % 2 === 0
  const third = integers[2] % 2 === 0

  if (first === second) {
    outlier = !first
  } else if (first === third) {
    outlier = second
  } else if (second === third) {
    outlier = first
  }

  for (let i of integers) {
    if ((i % 2 === 0) === outlier) {
      return i
    }
  }
}

// Using array.filter
function findOutlier2(integers) {
  const even = integers.filter((a) => a % 2 === 0)
  const odd = integers.filter((a) => a % 2 !== 0)
  return even.length === 1 ? even[0] : odd[0]
}

const testArray1 = [1, 5, 7, 13, 12, 19, 21]
const testArray2 = [2, 4, 6, 8, 11, 12, 14]

console.log(`Running: ${filename}`)
console.log(findOutlier(testArray1))
console.log(findOutlier(testArray2))
console.log('-----')
console.log(findOutlier2(testArray1))
console.log(findOutlier2(testArray2))
