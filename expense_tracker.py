categories = []
amounts = []

while True:
    print("============================")
    print("Expense Tracker")
    print("============================")
    print("1.Add Expense")
    print("2.View Expense")
    print("3.Show Total Expense")
    print("4.Show Highest Expense")
    print("5.Show Lowest Expense")
    print("6.Show Average Expense")
    print("7.Exit")


    option= input("Choose your option:")
    if option=="1":
     while True:
      category = input("Enter expense:")
      amount = float(input("Enter amount:"))
      categories.append(category)
      amounts.append(amount)
      user=input("Do you want to add another expense (yes/no):").lower()
      if user == "yes":
        continue
      else:
          break;
    elif option=="2":
        if len(categories)==0:
            print("No expenses found")
        else:
          for i in range(len(categories)):
            print(f"{categories[i]} :{amounts[i]}")
    elif option=="3":
        total=0
        for i in range(len(amounts)):
           total = total + amounts[i]
        print(f"Total Expense :{total}")
    elif option == "4":
        if len(amounts) ==0:
         print("No amounts")
        else:
         Highest = max(amounts)
         print(f"Highest Expense :{Highest}")
    elif option == "5":
        if len(amounts) ==0:
         print("No amounts")
        else:
         Minimum = min(amounts)
         print(f"Lowest :{Minimum}")
    elif option == "6":
        if len(amounts) == 0:
            print("No expense")
        else:
            total=0
            for i in range(len(amounts)):
                total = total + amounts[i]
            average =total/float(len(categories))
            print(f"Averages of Expenses:{average}")
            
        
    elif option=="7":
        print("Thank you for using Expense Tracker.")
        break
    else:
        print("Invalid option")
