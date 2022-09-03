accno = 11212
amount = 5000
def main():
   ac=int(input("enter the account number:"))
   if ac == accno:
      print("do you want to withdraw or deposit")
      op = int(input("Enter 1 for withdraw or Enter 2 for deposit:"))
      if op == 1:
         withdraw()
         us=int(input("anything else if yes press 1 or if no press 2 "))
         if us ==1:
            deposit()

      else:
         deposit()



def withdraw():
   global amount
   print("account number is :",accno)
   print("your amount balance is :", amount)
   wAmt = int(input("enter the amount to withdraw :",))
   balance = amount-wAmt
   amount=balance
   print("withdraw amount is:",wAmt)
   print("your balance is :",balance)


def deposit():
   global amount
   print("account number is:",accno)
   print("your amount is :", amount)
   dAmt =int(input("enter the amount to deposit:",))
   balance = amount+dAmt
   amount=balance
   print("deposit amount:",dAmt)
   print("your balance is :",balance)
   
main()