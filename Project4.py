#exchanging values
def exchange():
    
    a=int(input("Enter a number"))
    b=int(input("Enter another number"))
    
    temp=a
    a=b
    b=temp
    print(f"The new numbers are:{a,b}")
    return a,b
exchange()
