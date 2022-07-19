game_is_on = True
input_msg = ""
name = ""
from time import sleep 


# Defining room class
class Room:
  def __init__(self, name=None, description=None, objects=None, paths=None):
    self.name = name
    self.description = description


# Creating lists and dictionary   
room_list = []

characters = ["Damper", "Hush Puppy", "Johnny Cakes" ]

doors = ["Door 1", "Door 2", "Door 3",]

actions = ["Sincere", "Sarcastic"]

Jack = {

"memory": ["Deletion","Recovery", "Ascendance"],

"dialouge": ["Sincere", "Sarcastic"], 
  
}

room_1 = Room()
room_1.name = "Room 1"
room_1.description = '''
Once you open the door, you see a menacing humanoid figure who calls out to you '''

room_2 = Room()
room_2.name = "Room 2"
room_2.description = '''
When you enter the room, you feel a sense of unusual comfort that battles the confusion you are experiencing...'''

room_3 = Room()
room_3.name = "Room 3"
room_3.description = '''
Once you have entered the room, your expectations are broken as you do not feel anything. '''

room_list.append(room_1)
room_list.append(room_2)
room_list.append(room_3)

  

# Defining functions to be later used when game is on
def prompt_user():

       sleep(1)
       
       reply = input(''' 
                     
''')
       
       return reply
 
def check_answer(input):
       global name
       input_msg = input
 
       if "idk" in input_msg:
           sleep(2)
           print("Have you considered...  ")
           print("that your indecisive nature has led to more harm than good?")
           print("Make a proper decision this time.")
 
       elif "Room 1" in input_msg:
           global game_is_on
        
           sleep(1)

           print('''
You slowly approach the door and open it.''')
           sleep(1)
           print(room_1.description)
           sleep(2)
           print('''
Person: Hello,''' + name)
           sleep(1)
           print(''' 
Person: Long time no see''')
           sleep(1)  
           print(''' 
How do you respond?''')
           sleep(1)
           print(actions)         
           sleep(1)  
           test_string = input_msg: 
         
           if  "Sincere" in input_msg:
             print("That would make sense, if i had known who you were.");


           
       elif "Room 2" in input_msg:
           print("Greetings " + name)

       elif "Room 3" in input_msg:
           print("Salutions " + name)

  
       elif "none" in input_msg:
          print("... how dare you... allow me to show you what breaking the game is really like...")
          game_is_on = False 
  
       else:
           print("I wish i knew what that meant... try again...")


# Defining function that initiates beginning text during the start of the game    
def start():
   global name
   sleep(1)
   print("You are in a lush dark labryinth of... somewhere unknown... ")
   sleep(1)
   print('''             
Your sorroundings consist of nothing but 3 doors, all of them leading to territories unexplored''')

   name = (" Jack Cheese")
   sleep(1)
   print('''
You slowly come to remember that your name is Jack Cheese ''')
   sleep(1)
   print(''' 
Which room do you wish to proceed to?''')

  
   for room in room_list:
     print(room.name) 
   while game_is_on:
         check_answer(prompt_user())
         



  
start()


# The IF statement that ends the game & rolls credits after essential dialouge is complete 
if game_is_on == False: 

      sleep(2)

      print('''
|========Certificate of Death========|
|         Jack Fried Cheese          |
|   DOB: 4/20/69     DOD: 6/8/12     |  
| [Redacted]  [Redacted]  [Redacted] |                    
| [Redacted]  [Redacted]  [Redacted] |   
| [Redacted]  [Redacted]  [Redacted] |\n            
|____________________________________| ''')

      sleep(2)

print('''
      Credits:
      
      
Director: Luis Cardenas 
      
      He did everything...

      
     ''') 

sleep(2)

print("Jack will return...")

sleep(2)

if input() == "Sincere":
  print(Jack["Dialouge"][0])