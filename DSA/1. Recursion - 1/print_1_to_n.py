def print_1_to_n(n):
    if n==0:
        return
    else:
        print_1_to_n(n-1)
        print(n)
        return


n = int(input("Enter ANy Number: "))
print_1_to_n(n)
