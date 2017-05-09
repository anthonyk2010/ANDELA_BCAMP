def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  if type(n) == str: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True 

import unittest

class Prime_test(unittest.TestCase):
  def test_prime(self):
    self.assertEqual(is_prime(1), True)
    self.assertEqual(is_prime(1), False)
    self.assertEqual(is_prime(2), True)
    self.assertEqual(is_prime(2), False)
unittest.main()
