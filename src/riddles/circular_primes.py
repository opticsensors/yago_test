"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""

lim = 10**6
candidates = list(range(2,lim))

for i in range(len(candidates)):
    candidate = candidates[i]
    if candidate != None:
        try:
            while True:
                i += candidate
                candidates[i] = None
        except:
            pass
    else:
        pass

primes_map = []
for _ in candidates:
    if _ != None:
        primes_map.append(str(_))

rotation_inmune_primes = []

primes = primes_map.copy()

all_family = True
# Si 'False', devolverá únicamente la primera combinación de los primos
# rotacionales. Si 337 es primo rotacional, ni 733 ni 373 aparecerán
# en los resultados. En caso de establecerlo en 'True', aparecerán.

already_visited = []
for prime in primes:
    if prime not in already_visited:
        cbs_gen = (_ for _ in list(prime*(len(prime)+1)))
        cbs = []
        for _ in range(len(prime)):
            cb = ''
            for _ in range(len(prime)):
                cb += next(cbs_gen)
            cbs.append(cb)
            next(cbs_gen)
        if all([cb in primes for cb in cbs]):
            rotation_inmune_primes.append(prime)
            if all_family==False:
                for cb in cbs[1:]:
                    already_visited.append(cb)

print(rotation_inmune_primes)
            
        




a = 1

