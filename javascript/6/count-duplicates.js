/* Count Duplicates
 *
 * Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
 *
 * Example:
 *   "abcde" -> 0 # no characters repeats more than once
 *   "aabbcde" -> 2 # 'a' and 'b'
 *   "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
 *   "indivisibility" -> 1 # 'i' occurs six times
 *   "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
 *   "aA11" -> 2 # 'a' and '1'
 *   "ABBA" -> 2 # 'A' and 'B' each occur twice
 */

const path = require('path')
const filename = path.basename(__filename)

function duplicateCount(text) {
  const cache = {}
  let count = 0

  if (!text) {
    return 0
  }

  for (const i of text) {
    const char = i.toLowerCase()
    if (!cache[char]) {
      cache[char] = 1
    } else if (cache[char] === 1) {
      cache[char]++
      count++
    } else {
      cache[char]++
    }
  }
  return count
}

// Magic in the regex
function duplicateCount2(text) {
  return (
    text
      .toLowerCase()
      .split('')
      .sort()
      .join('')
      .match(/([^])\1+/g) || []
  ).length
}

console.log(`Running: ${filename}`)
console.log(duplicateCount(''))
console.log(duplicateCount('aabbcde'))
console.log('-----')
console.log(duplicateCount2(''))
console.log(duplicateCount2('aabbcde'))
