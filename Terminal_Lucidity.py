game_is_on = True
input_msg = ""
name = ""
 
def prompt_user():
       reply = input(" your sorroundings consist nothing but   3 doors, all of them leading to territories  ")
       return reply
 
def check_answer(input):
       global name
       input_msg = input
 
       if "help" in input_msg:
           print("Here are some commands you can try: .....")
           print("help, end, greet")
 
       elif "end" in input_msg:
           global game_is_on
           game_is_on = False
           print("Thank you for playing, goodbye!")
           
       elif "greet" in input_msg:
           print("Hello " + name)
 
       else:
           print("Sorry, I don't know what that means.")
 
def start():
   global name
   print("You are in the lush dark labryinth of... somewhere unknown... ");
   name = ("Jack LeFux")
   print("You slowly come to remember that your name is Jack LeFux");
 
   while game_is_on:
       check_answer(prompt_user())
 
start()