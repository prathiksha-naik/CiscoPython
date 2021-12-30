try:
    print('5'/10)
except ArithmeticError:
    print('arith')
except ZeroDivisionError:
    print('zero')
except:
    print('some')
