#Q2
total_terms=int(input("Enter total no. of terms:"))

def generateFibonacciSeq(total_terms):
    n1,n2 = 0,1
    i=2
    fib_sequence=[n1,n2]
    while i<total_terms:
        next_term=n1+n2
        fib_sequence.append(next_term)
        n1=n2
        n2=next_term
        i+=1
    print("Fibonacci Series:",fib_sequence)        
    
    
generateFibonacciSeq(total_terms)
    
    
