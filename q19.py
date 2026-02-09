#Write a function that returns if is a prime number and otherwise,using a loop
n=int(input("enter your number"))
for i in range(2,n):
    if n%i==0:
      print ("is _not prime")
    elif n%i!=0:
     print("is prime")

