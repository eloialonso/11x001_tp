n = int(input("Entrer un entier supérieur à 1: "))

i = 0
while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(n)
    i += 1

print("Temps de vol: ", i)
        
