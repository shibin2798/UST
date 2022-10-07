#Q6
sample_string=input("Enter a string:").upper()

def checkPallindrome(sample_string):
    if sample_string == sample_string[::-1]:
        print("Yes")
    else:
        print("No")

checkPallindrome(sample_string)
        
