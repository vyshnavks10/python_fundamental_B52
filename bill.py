pcost=eval(input("enter pizza cost:"))
c= "vyshnav"
v=input("enter the coupon code:")
if v==c:
    print("coupon code applied")
else:
    print("not vailed")
dis=15
damt=pcost*dis/100
finalcost=pcost-damt
q=int(input("enter quantity:"))
billamt=finalcost*q
print("discount:",damt)
print("final cost of pizza is:",finalcost)
print("quantity is :",q)
print("billamount:",billamt)
