beatles=[]
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
for i in range(1,3):
    user=input("Enter the name")
    beatles.append(user)
del beatles[3]
beatles.insert(0,"Ringo Starr")

# step 5
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
