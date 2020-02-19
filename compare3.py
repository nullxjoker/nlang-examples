import time

_start = time.perf_counter();

fib1 = 1
fib2 = 1
 
n = 5
 
i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
 
print('Fibo is ' + str(fib2))

print('Time: ' + str(time.perf_counter() - _start))