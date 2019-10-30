def findPrimes(n):
    a = []
    b = []
    for i in range(2,n+1):
        if i not in a:
            b.append(i)
            for j in range(i*i,n+1,i):
                a.append(j)
    return b
number = int(input("Enter a number please: "))
print(findPrimes(number))
