a = 4094
b = 8456

def sumOfOdd(num1, num2):
    x = [tnum1 for tnum1 in range(num1,num2+1) if tnum1%2 != 0]
    return sum(x)

print(sumOfOdd(a, b))