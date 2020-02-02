nl = list()

for i in range(0, 5):

    n = int(input('Digite um valor: '))

    if (i == 0 or n > nl[-1]):
        nl.append(n)
    else:
        pos = 0
        while pos < len(nl):
            if n <= nl[pos]:
                nl.insert(pos, n)
                break
            pos += 1

print(nl)