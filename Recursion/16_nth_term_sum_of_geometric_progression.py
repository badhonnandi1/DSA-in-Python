def geometricProg(a,r,n):
    if n==0:
        return 0
    else:
        return a*(r**(n-1)) + geometricProg(a,r,n-1)

a = int(input("Enter the first term: "))
r = int(input("Enter the common ratio: "))
n = int(input("Enter the nth term: "))
print(geometricProg(a,r,n))

# sample input: 2 3 4
