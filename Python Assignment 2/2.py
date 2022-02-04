"""
 Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""
n = 5
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print("\n")

for k in range(n, 0, -1):
    for l in range(k - 1, 0, -1):
        print("*", end=" ")
    print("\n")

