# x =lambda a,b:a+b
# print(x(5,2))
#
# def multiply(n):
#     return lambda a:a*n
# num1= multiply(6)
# print(num1(11))


#Calculate the value of mathematical expression x*(x+5)^2 where x= 5 using lambda expression
square =lambda x:x*(x+5)^2
print(square(5))
