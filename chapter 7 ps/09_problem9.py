n = int(input("Enter a number: "))


for i in range(1, n+1):
    if(i==1 or i==n):
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")


# n = 3

# for row in range(n):
#     if row == 0 or row == n - 1:
#         print("*" * n)
#     else:
#         print("*" + " " * (n - 2) + "*")