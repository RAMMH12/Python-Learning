num1 = int(input('Enter a number :'))
def factorial(num):
    for i in range(1,num):
        num=num*i
    print('Factorial of ',num1,' is: ',num)

factorial(num1)
