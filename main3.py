from typing import List, Iterator, Tuple
import operator
from collections import Counter
from functools import lru_cache
import time

# キャッシュの学習

@lru_cache
def long_func(num: int) -> int:
  r = 0
  for i in range(10000000):
    r += num * i
  return r

# if __name__ == '__main__':
#   for i in range(10):
#     print(long_func(i))

#   start = time.time()
#   for i in range(10):
#     print(long_func(i))
#   print(time.time() - start)


def memoize(f):
  def _wrapper(n):
    print("before")
    r = f(n)
    print("after")
    return r
  return _wrapper

@memoize
def test(n):
  print("test")

print(test(10))