''' You've surely seen a seven-segment display.

It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.

Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

Each digit is constructed from 13 LEDs (some lit, some dark, of course) - that's how we imagine it:

  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###

Note: the number 8 shows all the LED lights on.

Your code has to display any non-negative integer number entered by the user.

Tip: using a list containing patterns of all ten digits may be very helpful.

Test data
Sample input:

123

Sample output:

  # ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ### 

Sample input:

9081726354

Sample output:

### ### ###   # ### ### ### ### ### # # 
# # # # # #   #   #   # #     # #   # # 
### # # ###   #   # ### ### ### ### ### 
  # # # # #   #   # #   # #   #   #   # 
### ### ###   #   # ### ### ### ###   # 

'''
def numToLed(digits):
	lines = [ '' for l in range(5) ]	
	for num in digits:
		parttern = leds[int(num)]
		#Each segment has 3 "leds"
		segment = [[" "," "," "] for s in range (5)]
		#depending each digit of the parttern, turning each led of the segment ON (assigning the # to the segment.)
		if parttern[0] == "1":
			segment[0][0] = segment[0][1] = segment[0][2] = "#"

		if parttern[1] == "1":
			segment[0][2] = segment[1][2] = segment[2][2] = "#"

		if parttern[2] == "1":
			segment[2][2] = segment[3][2] = segment[4][2] = "#"

		if parttern[3] == "1":
			segment[4][0] = segment[4][1] = segment[4][2] = "#"

		if parttern[4] == "1":
			segment[2][0] = segment[3][0] = segment[4][0] = "#"

		if parttern[5] == "1":
			segment[0][0] = segment[1][0] = segment[2][0] = "#"

		if parttern[6] == "1":
			segment[2][0] = segment[2][1] = segment[2][2] = "#"

		#putting segments of each digit to a list called lines
		#lines is a 5 element list, which each element represents the row should be printed out on the console
		preDisplay(lines,segment)
	else:
		ledDisplay(lines)


print(numToLed(9081726354))
