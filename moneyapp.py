something = []
def addexpense():

  while True:
    #ask user for expense, amount, description and type
    expense=input("What is the expense?\n")
    amount=input("How many?")
    description=input("Description?")
    its=input("What type?")
    #print saying what you have
    print(f"You have {amount} {description} {its} {expense}")
    #the bank
    bank = {"expense": expense, "amount" : amount, "description" : description, "its" : its}
    #add dictionary to list
    something.append(bank)
    #ask if user wants to continue or stop
    answer = input("Do want more powerful stuff?")
    if answer == "yes":
      #make it keep on going
      continue
    else:
      #stop it
      break
  
#this function looks at the expenses
def viewexpenses():
  for j in something:
    print(j)
    
def viewbycategory():
  for i in something:
      print(i["its"])
  c2 = input("What category?")
  for k in something:
    if c2 == k["its"]:
      print(k)
def saveexpenses():
  t=open("practice.py","w")
  for s in something:
    y = f"Description =  {s['description']},its =  {s['its']},amount =  {s['amount']},expense =  {s['expense']}\n"
    t.write(y)
  print("Your expenses are saved.")
  
    
    
#Users input
def main():
  print("/---\ \n|| ||! Hello! Welcome to GMYM(Give Me Your Money!")
  while True:
    c1 = input("Choose an option:\n 1.Add\n 2.View\n 3.Calculate\n 4.View by Category\n 5.Save\n 6.Quit\n Enter your choice:\n")
    if c1 == "1":
      addexpense()
    elif c1 == "2":
      viewexpenses()
    elif c1 == "4":
      viewbycategory()
    elif c1 == "5":
      saveexpenses()
    elif c1 == "6":
      break

main()
