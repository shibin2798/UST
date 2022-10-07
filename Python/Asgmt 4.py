#Inches to Meters Conversions

length_inches = int(input("Enter length in inches:"))

length_meters=length_inches/39.37
meters = int(length_meters//1)
centimeters = str(length_meters).split('.')
print(length_inches,"inches=",meters,"meters and",only_cm[0:2],"centimeters")
