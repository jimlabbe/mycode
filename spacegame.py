#!/usr/bin/python3
import os
# Replace RPG starter project with this code when new instructions are live
os.system("clear")
print('PARHELION: A SPACE SURVIVAL GAME')
name = input('Enter your name?')

def showInstructions():
  #print a main menu and the commands
  print("""
========
You are a junior engineer aboard the Parhelion, bound towards a deep space terraforming 
colony. After the Parhelion escapes orbit, you enter your autohomeostasis pod to spend a 
majority of the trip in peaceful sleep. You awaken groggily as the emergency awaken injects you with the combination of restoratives, and your pod cracks open slightly. The stinging
acrid smell of burnt metal seeps into your pod. If you push your pod door, you can
probably free yourself from the pod. """)
  input("Try, 'push pod'")

  print("""
As you push the pod open, the wristband of
your bodysuit flashes, and you see the OXYGEN meter drop from 100% down to 99%.
Commands:
  go [direction]
  get [item]
  look []
  examine [object]
""")

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('Oxygen saturation is at', oxy, '%')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
 # if "item" in rooms[currentRoom]:
 #   print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []
body = int(3)
skills = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
def objects(target):
    if currentRoom == 'Crew Stasis Bay 9':
        if target == 'console':
            print('its a console')
        elif target == 'pod':
            print('theres a tool under the pod')
        return 0
    elif room == 'passage':
        print('youre in a passage')
    return 0
        


rooms = {

            'Crew Stasis Bay 9' : {
                  'south' : 'P-Way',
                  'east'  : 'Utility Locker',
                  'item'  : 'L-tool',
                  'object'  : {
                      'console',
                      'pod',
                              },
                },

            'P-Way' : {
                  'north' : 'Hall',
                  'south' : 'Bridge',
                  'item'  : 'monster',
                },
            'Utility Locker' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            }
         }

#start the player in the Hall
currentRoom = 'Crew Stasis Bay 9'

showInstructions()
oxy = int(101)
#loop forever
while True:
  oxy -= 2
  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first

#if player looks for something
  if move[0] == 'look':
    objects(move[1])
  else:
    print("It's not worth looking at")

  #if they type 'get' first
  if move[0] == 'get':
    #if the room contains an item, and the item is the one they want to get
    if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
 
  ## Define how a player can win
  if currentRoom == 'bridge' and 'key' in inventory and 'potion' in inventory:
    print('You push the button and the whole ship trembles as it is pulled towards a wonderous destinations...YOU WIN!!')
    break

  ## If player gets hurt enough times
  if body <= 0:
    print("Your body is unable to sustain any more damage...you die.")
    break
  ## If a player runs out of air
  elif oxy <= 0:
    print('gasping for air, darkness creeps in from the edges of your vision... GAME OVER!')
    break
