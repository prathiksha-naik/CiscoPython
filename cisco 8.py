blocks = int(input("Enter the number of blocks: "))
height = 0
inlayer = 1
while inlayer <= blocks:
	height += 1
	#print(f"{inlayer}  height {height}")
	blocks -= inlayer
	#print(f"blocks {blocks}")
	inlayer += 1
	#print(f"inlayer {inlayer}")
	#print("***************************************************")
print("Height of the pyramid:",height)
