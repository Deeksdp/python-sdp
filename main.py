#write a function to calculate nth power of a number
#return the result from the function and print the result
def power():
  a=int(input("Enter the number"))
  b=int(input("Enter the power"))
  c= a**b
  print(f"the power is {c}")
  return c
power()