result1 = int(input())
result2 = int(input())
x = result1 > 0
y = result2 > 0

if (x and y):
    print("1")
elif (not x and y):
    print("2")
elif (not x and not y):
    print("3")
elif (x and not y):
    print("4")
        