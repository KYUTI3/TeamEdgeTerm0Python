# -------------------------------------------- 

	# You've just learned about variables, conditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you get the bill. 

	# How do you think restaurants automate that math?

					# Let's try it!

# -------------------------------------------- 

# Scenario Parameters: 

	# When you eat out, you have the option to order one or multiple items.
	# What kind of items are available to order? There's usually a menu.
	# Allow your user to order a drink, meal, and dessert.

	# At the end of the order, the receipt comes and you have to calculate the total cost:
	# Don't forget the tax and tip!

# After this program finishes running, it should output a receipt with:
        #1. the items you ordered and their cost 
	#2. a total for your order before tax
	#3. a total for your order after tax
	#4. the amount of your tip 
	#5. the total including tax and tip

# -------------------------------------------- 
def menu():
  #Meals
  print("******Meals******")
  print("[0] Big Mac: $4")
  print("[1] Spicy Chicken Sandwhich: $5")
  print("[2] 10 Chicken Nuggets: $5")
  #Drinks
  print("******Drinks******")
  print("[3] Hi-C: $2")
  print("[4] Pepsi: $3")
  print("[5] Coke: $3")
  #Dessert
  print("******Desserts******")
  print("[6] McFlurry: $3")
  print("[7] Vanilla Cone: $1")
  print("[8] Hot Fudge Sundae: $2")

# -------------------------------------------- 

# Part 1:
# Let's start by creating the variables we'll need to keep track of the user's order
# as well as TAX and tip

# Remember: Your user should be able to order at least 3 items (a drink, meal, and dessert item). 

# --------------------------------------------



meal = 0
drink = 0
dessert = 0
total = 0

print("\nWhat would you like to order today?\n")
menu()
order1 = input("\nMeal: ")
print(order1)
amount1 = input("Amount: ")
order2= input("Drinks: ")
amount2 = input("Amount: ")
order3= input("Desserts: ")
amount3 = input("Amount: ")
def meal():
  meal = 0
  if(int(order1) == 0): 
    meal = 4 #4 = cost added
  elif(int(order1) == 1):
    meal = 5 #5 = cost added
  elif(int(order1)== 2):
    meal = 5
  meal *= int(amount1)
  return meal
def drinks():
  drinks = 0
  if(int(order2) == 3):
    drink = 2
  elif(int(order2) == 4):
    drink = 3
  elif(int(order2) == 5):
    drink = 3
  drinks *= int(amount2)
  return drink

def dessert():
  dessert = 0
  if(int(order3) == 6):
    dessert = 3
  elif(int(order3) == 7):
    dessert = 1
  elif(int(order3) == 8):
    dessert = 2
  dessert *= int(amount3)
  return dessert

print(meal())
def tax():
  #total += (int(total))*.1)
  print("Total after tax" + str(total))


  
# -------------------------------------------- 

# Part 2:
# Next, let's display the menu. Include the food item name and it's cost. 

# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------






# -------------------------------------------- 

# Part 3:
# Let's take the order. What did the user order? What does it cost?

# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------












# -------------------------------------------- 

# Part 4:
# Now that you have the costs of everything ordered, let's calculate the cost of the order(including tip and tax).

# Write a function that will calculate the cost of the order, including:
# - Cost of all  ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 












# -------------------------------------------- 

# Part 5:
# Let's print out a receipt.

# Write a function that will take the values of the order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Tax for the order
# - Tip for the order
# - Total cost for the order


# -------------------------------------------- 




# -------------------------------------------- 

# Part 6: Food Order Bot

# Call all of your functions to get your food order bot up and running!

# --------------------------------------------







# -------------------------------------------- 

# Part 7: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering valid values. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.
# - Implement a rewards system (stamp cards, buy one get one, etc)

# --------------------------------------------
