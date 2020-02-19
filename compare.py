import time

_start = time.perf_counter();
a = abs(int(16));
suma = 0;

mult = 1;

while a > 0:
  digit = a % 10;
  suma += digit;
  mult *= digit;
  a = a // 10;

print('Sum: ' + str(suma));
print('Mul: ' + str(mult));
print('Time: ' + str(time.perf_counter() - _start))