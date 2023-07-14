#exception handling
try:
    n1=int(input('enter a number:'))
    n2=int(input('enter a another number:'))
    n=n1/n2
except ValueError:
    print('invalid number')
except ZeroDivisionError:
    print('zerror occured')
finally:
    print('the result is come:')
