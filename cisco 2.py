'''if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.'''
income = float(input("Enter the annual income: "))
if (10000<= income <= 85528):
    Tax = ((income*18)/100)-556.2
elif income >= 85528: 
    Tax =((income- 85528)*32)/100+14839.2
elif (-100 <= income<=1000): 
    Tax = 0.0
Tax = round(Tax, 0)
print("The tax is:", Tax, "thalers")
