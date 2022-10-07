#Q7
email=input("Enter you EmailID:")

def emailVerification(email):
    if (email[:1] != "@" and email[:1] != ".") and (email.count('@',)<=1 and email.count('.',)<=1):
        print(email,"is valid")
    else:
        print(email,"is invalid")


emailVerification(email)
