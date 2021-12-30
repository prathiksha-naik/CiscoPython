#break statement
def large(largest,count):
    while True:
        num=int(input("Enter a number or type -1 to end program: "))
        if num==-1:
            break
        count=count+1
        if num>largest:
            largest=num
    if count!=0:
        print(f"The largest number is {largest}")
    else:
        print("Didnt entered any number")

#continue statement
def largest(largest,count):
    number = int(input("Enter a number or type -1 to end program: "))
    while number != -1:
        if number == -1:
            continue
        count += 1

        if number > largest:
            largest= number
        number = int(input("Enter a number or type -1 to end program: "))

    if count:
        print("The largest number is", largest)
    else:
        print("You haven't entered any number.")


a=large(-999999999,0)
b=largest(-999999999,0)

