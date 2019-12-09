import numpy as np

def fib(n):
  if n < 2 and n > -2:
      return n
  neg = False
  if n < 0:
      neg = True
      n = abs(n)

  arr = np.matrix([[0,1],[1,1]], dtype=object)
  arrp = pow(arr, n-1)
  res = arrp * np.matrix([[0],[1]])
  return -long(res[1]) if neg and (abs(n)+1) % 2 != 0 else long(res[1])