result=int(input())
if result%400 == 0:
    print('1')
elif result%4 == 0 and not result%100 == 0 :
    print('1')
else :
    print('0')