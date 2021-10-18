# ciąg fibonacciego to ciąg, w którym dwa pierwsze wyrazy to 1, a kazdy kolejny wyraz to suma dwóch poprzednich
n = int(input("Podaj ile wyrazów ciągu fibonacciego chcesz zobaczyć?"))
f = []

f = [1,1]

for i in range (0, n - 2):
    print(i)

    f.append(f[i] + f[i + 1])

print(f)
