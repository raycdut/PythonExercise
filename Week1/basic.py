def TestFun():
    for i in range(1, 10, 2):
        if i % 5 == 0:
            print("Bingo")
            break
        else:
            print(i)


'''TestFun()'''


def foo(num, base):
    if(num >= base):
        foo(num // base, base)
    print(num % base, end=' ')

'''
numA = int(input())
numB = int(input())
foo(numA, numB)
'''