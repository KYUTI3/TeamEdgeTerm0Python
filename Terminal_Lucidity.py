game_is_on = True
input_msg = ""
name = ""
from time import sleep 
 
def prompt_user():
       print("your sorroundings consist of nothing but 3 doors, all of them leading to territories unexplored")
       sleep(2)
       reply = input("Which door do you traverse through?")
       
       return reply
 
def check_answer(input):
       global name
       input_msg = input
 
       if " door 1" in input_msg:
           print("Here are some commands you can try: .....")
           print("help, end, greet")
 
       elif " door 2" in input_msg:
           global game_is_on
           game_is_on = False
           print("Thank you for playing, goodbye!")
           
       elif " door 3" in input_msg:
           print("Hello " + name)

       elif "none" in input_msg:
          print("... how dare you... allow me to show you what breaking the game is really like...")
          game_is_on = False 
  
       else:
           print("I wish i knew what that meant... try again...")
 
def start():
   global name
   print("You are in a lush dark labryinth of... somewhere unknown... ");
   name = ("Jack LeFux")
   print("You slowly come to remember that your name is Jack LeFux");
 
   while game_is_on:
       check_answer(prompt_user())

      
start()

if game_is_on == False: 

      sleep(2)

      print('''
|________Certificate of Death________|
|         Jack Cheese LeFux          |
|   DOB: 4/20/69     DOD: 6/9/12     |  
| [Redacted]  [Redacted]  [Redacted] |                    
| [Redacted]  [Redacted]  [Redacted] |   
| [Redacted]  [Redacted]  [Redacted] |\n           
|====================================| ''')

print('''
      Credits:
      