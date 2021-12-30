def func(number1,number2):
    if number2>number1:
        return number1,number2
    else:
        return number2,number1
smaller,larger=func(666,23)
print(f"The smallest number is {smaller} and largest number is {larger}")
