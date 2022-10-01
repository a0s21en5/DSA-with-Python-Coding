def even(n):
    if n == -1:
        return
    else:
        even(n-1)
        print(n*2)


n = int(input("Enter Any Number : "))
even(n)
