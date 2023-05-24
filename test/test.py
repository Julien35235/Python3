#By Julien Despagne
n=2019
Liste = []
while (n != 0):
    i = 0
    while (2**i <= n):
        i = i + 1
    i = i - 1
    n = n-2**i
    Liste.append(2**i)
print(Liste, sum(Liste))