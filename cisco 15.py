list1=[]
num=int(input('Enter the numbers required for you in list: '))
for k in range(num):
    print("Enter the value: ")
    list1.append(int(input()))
#If 4 numbers are there in list we must compare 3 times so length of list minus one
print("Unsorted list",list1)
for j in range(len(list1)-1):
    for i in range(len(list1)-1-j):
        if list1[i]>list1[i+1]:#compare  adjacent elements 
            list1[i],list1[i+1]=list1[i+1],list1[i]#swap the number if it is greater
print("sorted list",list1)
    
