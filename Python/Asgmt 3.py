#Degrees-Farenhait Conversion
num = int(input("Enter a number:"))
conversion_type = input("Enter the conversion type:")

if (conversion_type == "F"):
    fahrenheit = num*(9/5)+32
    print(num,"celcius =",fahrenheit,"fahrenheit")
else:
    celcius = (num-32)*(5/9)
    print(num,"fahrenheit =",celcius,"celcius")
    
