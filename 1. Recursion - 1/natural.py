def sum_of_natural(n):
    if n == 0:
        return 0
    else:
        return n+sum_of_natural(n-1)


a = int(input("Enter Any Number: "))
print(sum_of_natural(a))
