def odd(n):
    if n == 0:
        return
    else:
        odd(n-1)
        print(n*2-1)


n = int(input("Enter Any Number : "))
odd(n)
