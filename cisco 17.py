mylist=[]
num=int(input("Enter the number to list"))
for i in range(num):
    print("Enter the value: ")
    mylist.append(int(input()))
print(mylist)
find=int(input("Which number do yu need to find in list: "))
found=True
for i in range(len(mylist)):
    found=mylist[i]==find
    if found:
        break
if found:
    print(f"The number {find} is found in list")
print("Ooops!The number is not found")
  
