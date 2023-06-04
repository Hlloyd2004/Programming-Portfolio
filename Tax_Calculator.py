print("Hello there. \nThis is my tax calcualtor program.\nI will calculate the tax as well as calculate the income you will have left after the tax has been taken out.\n")
option = "yes"
while option == "yes":
  income = float(input("Please enter your annual income: \n")) # The users income

# Tax dosnt need to be paid.
  if income <= 12570.00:
    tax = 0.00

# 20% is taken off income
  if income > 12570.00:
    if income < 50270:
    	  tax = income * 0.20

# 40% is taken off income
  if income >= 50270.00 and income < 125140.00:
      tax = income * 0.40

# 45% is taken off income
  if income > 125140.00:
    tax = income * 0.45
    
  tax = round(tax, 2) # Rounds the calculated tax to 2.dp
  print("The tax is", tax, "pounds")
    
  total = income - tax # Works out the total income after deducted tax
  rounded_total = round(total, 2) # Rounds the total into a currency format
  print("This makes your new annual income", rounded_total, "pounds\n")

  option = input("Would you like to enter a different annual income?")
  # This option is used so that the while loop can carry on.
  option.lower() # Changes the input into lowercase format.
  if option == "yes":
    print("That's great!")

  else: # Backup option to stop errors.
    print("Thank you for using the tax calculator!!")
    break