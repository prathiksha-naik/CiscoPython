text1=input("enter the string")
text2=input("enter the string")
text3=text2.split()
text=text1.split()
for i in range(len(text)):
    if text[i]=='a' or text[i]=='e' or text[i]=='i' or text[i]=='o' or text[i]=='u':
        result='YES'
        break
    else:
        result='NO'
for j in range(len(text3)):
    if text3[j]=='a' or text3[j]=='e' or text3[j]=='i' or text3[j]=='o' or text3[j]=='u':
        res='YES'
        break
    else:
        res='NO'
if result=='YES':
    print('YES')
else:
    print('NO')

if res=='YES':
    print('YES')
else:
    print('NO')
    

