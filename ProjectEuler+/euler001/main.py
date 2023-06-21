#!/usr/bin/env python3


if __name__ == '__main__':
    def multiples(j):
      '''
      finding the multiples of 3 or 5.
      time complexity of O(1)
      '''

      j -= 1 # confirming that `j` is always less of the number
      threes = (3 * (j // 3) * ((j // 3) + 1)) // 2 # calculating the sum multiples 3
      fives = (5 * (j // 5) * ((j // 5) + 1)) // 2 # calculating the sum multiples 5
      fifteen = (15 * (j // 15) *((j // 15) + 1)) // 2 # Calculating the sum of both 3 and 5
      total = threes + fives - fifteen
      return total
