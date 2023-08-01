class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 50000")

    def withdrawl(self,amount):
        new_amount = 50000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))
def main():
    Card_number = input("Insert Card Number:")
    Pin_number = input("Insert Pin Number:")
    new_users = Atm(Card_number,Pin_number)
    print("Choose your activity ")
    print("1.Balance Enquriy 2.withdrawl")
    activity = int(input("Enter Activity Number: "))
    if (activity==1):
        new_users.check_balance()
    elif(activity==2):
        amount = int(input("Enter The Amount: "))
        new_users.withdrawl(amount)
    else:
        print("Enter A Valid Number: ")
if __name__ == "__main__":
    main()