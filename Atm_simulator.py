initial_bal = 200000
task = None

while task != 4:
    
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")
    
    
    task = int(input("Enter Task: "))
# while task != 4: 
    if task == 1:
            deposit = int(input("Enter deposit: "))
            initial_bal = initial_bal + deposit
            print("New balance: {}" .format(deposit))
    elif task == 2:
            withdraw = int(input("Enter withdrawal amount: "))
            initial_bal = initial_bal - withdraw
            print("New balance: {}" .format(withdraw))
    elif task == 3:
            print(initial_bal)
    elif task == 4:
        break
    else:
        print("Invalid option")



   

