 def printing(num):
    if(num==1 or num==0):
        return 1
    elif(num!=1):
        return num*printing(num-1)
number=int(input("enter a number to find its factorial "))
print("the factorial of",number,"is",printing(number))
