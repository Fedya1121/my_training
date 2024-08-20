numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        numbers.remove(i)
        for j in (2, i):
            print({i % j})
            if i % j == 0:
                break
"""
2%2
3%2
4%2
4%3
5%2
5%3
5%4                
"""