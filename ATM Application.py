#ATM Project
while true:
    account=100000
    pwd=1234
    card=int(input("insert the card"))
    if card=="c":
        print("welcome srujana")
        password=int(input("enter the password"))
        if password==pwd:
            option=int(input('''choose the option
                             1.blance enq
                             2.withdraw'''))
            if option==1:
                       print("acc bal is",account)
            elif option==2:
                money=int(input("enter the amount"))
                print(money)
                balance=account-money
                print("rem acc bal is",blance)
            else:
                print("Invalid option")
        else:
            print("incorrect password")
    else:
        print("Invalid card")
