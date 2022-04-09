# p,q,r=int(input("enter 1st number:")),int(input("enter the 2nd number")),int(input("enter the3rd number"))
# if p>q and p>r:
#     print("first number is greater than other two:",p)
# elif q>r:
#     print("second number is greater than other two:",q)
# else:
#     print("thrid number is greater than other two:",r)

#print(max(map(int, (input('1st number: '), input('2nd number: '), input('3rd number: ')))))

a, b, c= int(input('enter first number')), int(input('enter second number')), int(input('enter third number'))
nums= [a, b, c]
print(max(nums))
