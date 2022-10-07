#Q5
demo_str= """Python is a widely used general-purpose,
high level programming language. It was created by Guido van Rossum in 1991
and further developed by the Python Software Foundation.
It was designed with an emphasis on code readability, and its syntax allows
programmers to express their concepts in fewer lines of code"""

demo_str.lower()
consonant_count=0
for i in range(0,len(demo_str)):
    if demo_str[i]>'a' and demo_str[i]<='z':
        consonant_count+=1
print("Count of consonants:",consonant_count)
for vowel in 'aeiou':
    print("Count of",vowel,":",demo_str.count(vowel))
    



