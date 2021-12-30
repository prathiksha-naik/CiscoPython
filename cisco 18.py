#Your task is to write a program which removes all the number repetitions from the list.The goal is to have a list in which all the numbers appear not more than once.
mylist=[]
user=int(input("Enter how many values required in your list"))
for i in range(user):
    print("Enter the value : ")
    mylist.append(int(input()))
print(mylist)
list1=[]
for i in mylist:
    if i not in list1:
        list1.append(i)
print(list1)
