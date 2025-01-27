counter = 0


def fib_recursive(n):
    global counter
    counter += 1
    if n == 0 or n == 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


n = 10
print("Fib of", n, "=", fib_recursive(n))
print(f"Counter: {counter}")


""" 
#Using Memoization


memo = [None] * 100
counter = 0
def fib_memo(n):
    global counter
    counter += 1
    if memo[n] is not None:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

n = 7
print("Fib of", n, "=", fib_memo(n))
print(f"Counter: {counter}")

"""


"""
counter = 0

def fib_iterative(n):
    global counter
    fin_list = [0, 1]
    for i in range(2, n + 1):
        counter += 1
        fin_list.append(fin_list[i - 1] + fin_list[i - 2])
    return fin_list[n]


print(fib_iterative(10))
print(f"Counter: {counter}")
"""
