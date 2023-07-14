try:
    n1=int(input('enter a number:'))
    n2=int(input('enter a another number:'))
    result=n1/n2
except ValueError:
    print('invalid number')
except ZeroDivisionError:
    print('zero occurred')
else:
    print('the division was successful')
    print('result',result)
