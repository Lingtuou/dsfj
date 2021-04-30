import random as rd
n = int(input('要分解的数'))
r = 0
k = input('几轮测试？')
n -= 1
while n&1 == 0:
    n /= 2
    n = int(n)
    r += 1
#n = 2**r * n + 1
for i in range(k):
    a = rd.randint(2, 2**r * n - 1)
    x %= n
