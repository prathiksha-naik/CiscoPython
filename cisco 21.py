'''A car's fuel consumption may be expressed in many different ways. For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.
In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.Your task is to write a pair of functions converting l/100km into mpg,
and vice versa.the functions:are named liters_100km_to_miles_gallon and miles_gallon_to_liters_100km respectively;take one argument (the value corresponding to
their names)Complete the code in the editor.Run your code and check whether your output is the same as ours.Here is some information to help you:
1 American mile = 1609.344 metres;
1 American gallon = 3.785411784 litres.
Expected output
60.31143162393162
31.36194444444444
23.52145833333333
3.9007393587617467
7.490910297239916
10.009131205673757'''
def liters_100km_to_miles_gallon(liters):
    pass
#
# Write your code here.
#

def miles_gallon_to_liters_100km(miles_per_gallon):
    liters_per_gallon = 3.785411784
    kilometers_per_mile = 1.609344
    liters_per_100 = (100*liters_per_gallon)/(kilometers_per_mile*miles_per_gallon)
    print(miles_per_gallon,'miles per gallon are',liters_per_100,'liters per 100 kilometers.')

#
# Write your code here
#

liters_100km_to_miles_gallon(3.9)
liters_100km_to_miles_gallon(7.5)
liters_100km_to_miles_gallon(10.)
miles_gallon_to_liters_100km(60.3)
miles_gallon_to_liters_100km(31.4)
miles_gallon_to_liters_100km(23.5)
