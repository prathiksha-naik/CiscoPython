def convert_distance(miles):
    km=miles*1.6
    return km
def convert_distance2(km):
    miles= 0.621371*km
    return miles

my_trip_miles=convert_distance(55)
my_trip_km=convert_distance2(55)
print("The distance in kilometers is " ,my_trip_miles)
print("The round-trip in kilometers is " ,my_trip_km)
