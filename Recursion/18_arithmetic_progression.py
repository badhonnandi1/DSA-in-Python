def arithmeticProg(a,d,n):
    if n==0:
        return 0
    else:
        print(arithmeticProg(a,d,n-1))
        return (a+d*(n-1))

a = int(input("Enter the first term: "))
d = int(input("Enter the common difference: "))
n = int(input("Enter the nth term: "))
print(arithmeticProg(a,d,n))

# sample input: 2 3 4
