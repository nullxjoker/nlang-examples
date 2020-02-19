import time

_start = time.perf_counter();
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n
 
 
print(fac(20))
print('Time: ' + str(time.perf_counter() - _start))