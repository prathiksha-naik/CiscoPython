#finding largest number in list
mylist=[]
num=int(input("Enter how many value required in list: "))
for k in range(num):
    print("Enter the value: ")
    mylist.append(int(input()))
print(mylist)
largest=mylist[0]
for i in (1,len(mylist)-1):
    if mylist[i]>largest:
        largest=mylist[i]
print("The largest value in list is: ",largest)
