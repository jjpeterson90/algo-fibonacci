fib_memo = {}

def fibonacci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  if n not in fib_memo:
    fib_memo[n] = fibonacci(n-1) + fibonacci(n-2)
  return fib_memo[n]