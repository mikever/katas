const path = require('path')
const filename = path.basename(__filename)

/* Sum of Digits - Digital Root
 *
 * Digital root is the recursive sum of all the digits in a number.

 * Given n, take the sum of the digits of n. If that value has more than one digit, continue
 * reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
 * 
 * Examples
 *       16  -->  1 + 6 = 7
 *      942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
 *   132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
 *   493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
 */

function digitalRoot(num) {
  if (num < 10) return num

  // Applies Number constructor to each element
  const numArray = Array.from(num.toString()).map(Number)

  return digitalRoot(
    numArray.reduce((acc, curr) => {
      return acc + curr
    }, 0),
  )
}

function digitalRoot2(num) {
  if (num < 10) return num

  return digitalRoot2(
    num
      .toString()
      .split('')
      .reduce((acc, curr) => acc + +curr, 0), // +string casts to number
  )
}

console.log(`Running: ${filename}`)
console.log(digitalRoot(16) === 7)
console.log(digitalRoot(456) === 6)
console.log('-----')
console.log(digitalRoot2(16) === 7)
console.log(digitalRoot2(456) === 6)
