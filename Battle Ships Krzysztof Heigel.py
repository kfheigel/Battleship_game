#INFO
#every line with "TESTESTESTESTEST" is used to see the results of how the game works, if you want to see certain values, you need to uncomment those lines
# in computer_random_ship function there are two commented line, where if you want to see location of the computer ships, you need to uncomment those two commented lines

from tkinter import *
from tkinter import messagebox
from random import *
from math import *
import webbrowser

letter=["A","B","C","D","E","F","G","H","I","J"]
click_count = 0
click_change_direction = 0
click_game = 0
count_down = 3
player_score = 0
computer_score = 0

player_ship_position   = []
computer_ship_position = []

computer_miss_position = []
computer_hit_position  = []
computer_free_space    = []

player_miss_position   = []
player_hit_position    = []
player_free_space      = []


#***************************Functions********************************

# Function is checking if someone won the game
def winning_conditions():
     global computer_ship_position
     global player_ship_position
     global player_score
     global computer_score

     if ((len(computer_ship_position)==0) and (click_count >=10)):
          if messagebox.askyesno("PLAYER WON THE GAME", "Do you want to play again?"):
               player_score += 1
               reset_game()
          else:
               close_window()
     elif ((len(player_ship_position)==0) and (click_count >=10)):
          if messagebox.askyesno("COMPUTER WON THE GAME", "Do you want to play again?"):
               computer_score += 1
               reset_game()
          else:
               close_window()

# Function randomizing position of computer ships
def computer_random_ship(times,exception):
     global computer_ship_position
     global computer_free_space
     
     temp_position = []
     position      = randrange(2)
     
     if (position == 1):
          row = randrange(10-exception)
          col = randrange(10)
          for i in range(times):
               temp_position.append((row+i,col))
               #print(temp_position)#TESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTES
          if((not[el for el in computer_ship_position if el in temp_position]) and (not[el for el in computer_free_space if el in temp_position])):
               for i in range(times):
                    #button_computer[row+i][col].configure(bg="black", relief=SUNKEN)#TESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTES
                    computer_ship_position.append((row+i,col))
                    #adding free space around the ship
                    computer_creating_free_space_around_ship(position, row, col, times, i)
          else:
               computer_random_ship(times,exception)
     else:
          row = randrange(10)
          col = randrange(10-exception) 
          for i in range(times):
               temp_position.append((row,col+i))
          if((not[el for el in computer_ship_position if el in temp_position]) and (not[el for el in computer_free_space if el in temp_position])):
               for i in range(times):
                    #button_computer[row][col+i].configure(bg="black", relief=SUNKEN)#TESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTES
                    computer_ship_position.append((row,col+i))
                    #adding free space around the ship
                    computer_creating_free_space_around_ship(position, row, col, times, i)           
          else:
               computer_random_ship(times,exception)
          
#Checking if computer on players map hits or misses!!!!!!!!!!!!!!!!!!!!!!!!!!!   
def computer_ship_hits(row,col):
     global click_count
     if (click_count > 9):
          if((row,col) in computer_ship_position):
               button_computer[row][col].configure(bg="red", state=DISABLED, relief=SUNKEN)
               computer_hit_position.append((row,col))
               computer_ship_position.remove((row,col))
               label_7.configure(text="HIT",fg="red")
          elif((row,col) not in computer_miss_position):
               button_computer[row][col].configure(bg="blue", state=DISABLED, relief=SUNKEN)
               computer_miss_position.append((row,col))
               label_7.configure(text="MISS",fg="black")
          else:
               label_7.configure(text="YOU'VE ALREADY HIT THIS PLACE")

#Checking if on computers map there is a hit or miss          
def player_ship_hits():
     global click_game
     if (click_game <100):
          row = randrange(10)
          col = randrange(10)
          if ((row,col) not in player_hit_position):
               if((row,col) in player_ship_position):
                    button_player[row][col].configure(bg="red",state=DISABLED, cursor="left_ptr", relief=SUNKEN)
                    player_hit_position.append((row,col))
                    player_ship_position.remove((row,col))
               elif((row,col) not in player_miss_position):
                    button_player[row][col].configure(bg="blue", state=DISABLED, cursor="left_ptr", relief=SUNKEN)
                    player_hit_position.append((row,col))
          else:
               player_ship_hits()
     else:
          if messagebox.showwarning("End of Game","Game has ended"):
               reset_game()
     
#Displaying which ship is next to place on players map
def display_ship(c_count,c_change_direction):
     if (c_change_direction%2 == 0):
          if (c_count < 4):
               button_display[2][2].configure(bg="black")
               label_4.configure(text=str(4-c_count)+" SHIPS TO GO")
          elif(c_count < 7):
               for i in range(2):
                    button_display[i+1][2].configure(bg="white")
                    button_display[2][i+1].configure(bg="black")
               label_4.configure(text=str(7-c_count)+" SHIPS TO GO")
          elif(c_count < 9):
               for i in range(3):
                    button_display[i+1][2].configure(bg="white")
                    button_display[2][i+1].configure(bg="black")
               label_4.configure(text=str(9-c_count)+" SHIPS TO GO")
          elif(c_count < 10):
               for i in range(4):
                    button_display[i+1][2].configure(bg="white")
                    button_display[2][i+1].configure(bg="black")
               label_4.configure(text=str(10-c_count)+" SHIPS TO GO")                 
          elif(c_count >= 10):
               for i in range(4):
                    button_display[i+1][2].configure(bg="white")
                    button_display[2][i+1].configure(bg="white")
               label_4.configure(text=str("NO MORE SHIPS TO GO"))
     else:
          if (c_count < 4):
               button_display[2][2].configure(bg="black")
               label_4.configure(text=str(4-c_count)+" SHIPS TO GO")
          elif(c_count < 7):
               for i in range(2):
                    button_display[2][i+1].configure(bg="white")
                    button_display[i+1][2].configure(bg="black")
               label_4.configure(text=str(7-c_count)+" SHIPS TO GO")
          elif(c_count < 9):
               for i in range(3):
                    button_display[2][i+1].configure(bg="white")
                    button_display[i+1][2].configure(bg="black")
               label_4.configure(text=str(9-c_count)+" SHIPS TO GO")
          elif(c_count < 10):
               for i in range(4):
                    button_display[2][i+1].configure(bg="white")
                    button_display[i+1][2].configure(bg="black")
               label_4.configure(text=str(10-c_count)+" SHIPS TO GO")
          elif(c_count >= 10):
               for i in range(4):
                    button_display[2][i+1].configure(bg="white")
                    button_display[i+1][2].configure(bg="white")
               label_4.configure(text=str("NO MORE SHIPS TO GO"))

#changing direction of a ship on "screen" (vertical, horizontal)          
def change_direction():
     global click_change_direction
     global click_count
     click_change_direction += 1
     if(click_change_direction%2==0):
          button_direction.config(text="Perpendicularly",relief="raised")
     else:
          button_direction.config(text="Horizontally",relief="raised")
     display_ship(click_count,click_change_direction)

# Function that creates a field around ship to avoid touching with other ships
def computer_creating_free_space_around_ship(position, row, col, times, i):
     global computer_free_space
     
     if (position == 1):
               computer_free_space.append((row-1,col))
               computer_free_space.append((row-1,col+1))
               computer_free_space.append((row-1,col-1))
               computer_free_space.append((row+times,col))
               computer_free_space.append((row+times,col+1))
               computer_free_space.append((row+times,col-1))
               computer_free_space.append((row+i,col+1))
               computer_free_space.append((row+i,col-1))
     else:
               computer_free_space.append((row,col-1))
               computer_free_space.append((row+1,col-1))
               computer_free_space.append((row-1,col-1))
               computer_free_space.append((row,col+times))
               computer_free_space.append((row+1,col+times))
               computer_free_space.append((row-1,col+times))
               computer_free_space.append((row+1,col+i))
               computer_free_space.append((row-1,col+i))

     computer_free_space = set(computer_free_space)
     computer_free_space = list(computer_free_space)
     #print("Computer ship position: ", computer_ship_position)#TESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTES
     #print("free space around computer ship: ", len(computer_free_space))#TESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTES

     
# Function that creates a field around ship to avoid touching with other ships
def creating_free_space_around_ship(position, row, col, times):
     global player_free_space
     
     if (position == 1):
          for i in range(times):
               player_free_space.append((row-1,col))
               player_free_space.append((row-1,col+1))
               player_free_space.append((row-1,col-1))
               player_free_space.append((row+times,col))
               player_free_space.append((row+times,col+1))
               player_free_space.append((row+times,col-1))
               player_free_space.append((row+i,col+1))
               player_free_space.append((row+i,col-1))
     else:
          for i in range(times):
               player_free_space.append((row,col-1))
               player_free_space.append((row+1,col-1))
               player_free_space.append((row-1,col-1))
               player_free_space.append((row,col+times))
               player_free_space.append((row+1,col+times))
               player_free_space.append((row-1,col+times))
               player_free_space.append((row+1,col+i))
               player_free_space.append((row-1,col+i))
     temp_list=[]

     for i in range((len(player_free_space))):
          rows,cols = player_free_space[i]
          if((rows >= 0 and rows <= 9) and (cols >= 0 and cols <= 9)):
               temp_list.append((rows,cols))
               
     player_free_space = set(temp_list)
     player_free_space = list(player_free_space)
     
     for i in player_free_space:
          rows,cols = i
          button_player[rows][cols].configure(state=DISABLED, cursor="left_ptr")     

def checking_distance_to_a_ship(position, row, col, times):
     check_list =[]
     global player_free_space
     global player_ship_position
     
     if (position == 1):
          for i in range(times):
               check_list.append((row+i,col))
          if((not[el for el in player_free_space if el in check_list]) and (not[el for el in player_ship_position if el in check_list])):   
               for i in range(times):
                    player_ship_position.append((row+i,col))
                    button_player[row+i][col].configure(bg="black", state=DISABLED, cursor="left_ptr", relief=SUNKEN)
               creating_free_space_around_ship(position, row, col, times)
               computer_random_ship(times,times-1)
          else:
               return False
     else:
          for i in range(times):
               check_list.append((row,col+i))
          if((not[el for el in player_free_space if el in check_list]) and (not[el for el in player_ship_position if el in check_list])):    
               for i in range(times):
                    player_ship_position.append((row,col+i))
                    button_player[row][col+i].configure(bg="black", state=DISABLED, cursor="left_ptr", relief=SUNKEN)
               creating_free_space_around_ship(position, row, col, times)
               computer_random_ship(times,times-1)
          else:
               return False

#clicked_player
def clicked_player(row, col):
     global click_count
     global click_change_direction
     global count_down
     global player_free_space
     
     position = click_change_direction%2
     
     if(count_down ==0):
          button_direction.config(text="NO MORE SHIPS TO GO", state=DISABLED, relief="sunken")
     if (click_count <11):
          if (position == 1):
               if (click_count < 4):
                    if (checking_distance_to_a_ship(position, row, col, 1)==False):
                         messagebox.showwarning("Warning","Place ship in another location!")
                         click_count -= 1
               elif(click_count < 7):
                    if ((row+1)>=10):
                         messagebox.showwarning("Warning","Place ship inside the map!")
                         click_count -= 1
                    elif(row+1)<10:
                         if (checking_distance_to_a_ship(position, row, col, 2)==False):
                              messagebox.showwarning("Warning","Place ship in another location!")
                              click_count -= 1 
               elif(click_count < 9):
                    if ((row+2)>=10):
                         messagebox.showwarning("Warning","Place ship inside the map!")
                         click_count -= 1     
                    elif(row+2)<10:
                         if (checking_distance_to_a_ship(position, row, col, 3)==False):
                              messagebox.showwarning("Warning","Place ship in another location!")
                              click_count -= 1
                              count_down += 1
               elif(click_count < 10):
                    if ((row+3)>=10):
                         messagebox.showwarning("Warning","Place ship inside the map!")
                         click_count -= 1     
                    elif(row+3)<10:
                         if (checking_distance_to_a_ship(position, row, col, 4)==False):
                              messagebox.showwarning("Warning","Place ship in another location!")
                              click_count -= 1
                              count_down += 1
          else:
               if (click_count < 4):
                    if (checking_distance_to_a_ship(position, row, col, 1)==False):
                         messagebox.showwarning("Warning","Place ship in another location!")
                         click_count -= 1
               elif(click_count < 7):
                    if ((col+1)>=10):
                         messagebox.showwarning("Warning","Place ship inside the map!")
                         click_count -= 1     
                    elif(col+1)<10:
                         if (checking_distance_to_a_ship(position, row, col, 2)==False):
                              messagebox.showwarning("Warning","Place ship in another location!")
                              click_count -= 1 
               elif(click_count < 9):
                    if ((col+2)>=10):
                         messagebox.showwarning("Warning","Place ship inside the map!")
                         click_count -= 1     
                    elif(col+2)<10:
                         if (checking_distance_to_a_ship(position, row, col, 3)==False):
                              messagebox.showwarning("Warning","Place ship in another location!")
                              click_count -= 1
                              count_down += 1
               elif(click_count < 10):
                    if ((col+3)>=10):
                         messagebox.showwarning("Warning","Place ship inside the map!")
                         click_count -= 1     
                    elif(col+3)<10:
                         if (checking_distance_to_a_ship(position, row, col, 4)==False):
                              messagebox.showwarning("Warning","Place ship in another location!")
                              click_count -= 1
                              count_down += 1
     click_count += 1
     display_ship(click_count,click_change_direction)
     if(click_count>=7 and click_count<11):
          label_5.configure(text="THE GAME WILL START IN " + str(count_down) + "...")
          count_down -=1
     
#clicked_computer     
def clicked_computer(row, col):
     global click_count
     global click_game
     global computer_ship_position
     if ((len(computer_ship_position)>0) and (click_count >=10)):
          button_computer[row][col].configure(bg="black", relief=SUNKEN)
          computer_ship_hits(row, col)
          click_game += 1
          label_5.configure(text=str(click_game)+"  ROUND")
          player_ship_hits()         
     else:
          messagebox.showinfo("Info", "The Game has not started yet")
          
     winning_conditions()

#TESTESTESTESTESTESTEST printing list of positions for hit and miss  TESTESTESTESTESTESTEST
     #print("player ship position: ",player_ship_position)#TESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTES
     #print("computers ship position: ",computer_ship_position, "\n")#TESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTES
     #print("Comp map miss  ", computer_miss_position)#TESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTES
     #print("Comp map hit   ", computer_hit_position, "\n")#TESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTES
     #print("player map miss", player_miss_position)#TESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTES
     #print("player map hit ", player_hit_position, "\n", "\n")#TESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTESTES

#start_game    
def credits_game():
    messagebox.showinfo("Information","Created by Krzysztof Heigel.")

#reset messagebox
def reset_message_box():
     if messagebox.askokcancel("Reset", "Do you want to reset the game?"):
          reset_game()
          
#reset score, and all the game ettings
def reset_score():
     global player_score
     global computer_score
     
     if messagebox.askokcancel("Reset Score", "Do you want to reset the score?"):
          player_score = 0
          computer_score = 0
          reset_game()
    
#resets all the data in the game except the score   
def reset_game():
     global click_count
     global click_change_direction
     global click_game
     global count_down
     global player_score
     global computer_score
     
     global player_ship_position
     global player_miss_position
     global player_free_space
     global player_hit_position
     
     global computer_ship_position
     global computer_miss_position
     global computer_free_space
     global computer_hit_position
     
          
     click_count = 0
     click_change_direction = 0
     click_game = 0
     count_down = 3
     
     player_ship_position   = []
     computer_ship_position = []

     computer_miss_position = []
     computer_hit_position  = []
     computer_free_space    = []

     player_miss_position   = []
     player_hit_position    = []
     player_free_space      = []
          
     label_4.configure(text=str("4 SHIPS TO GO"))
     label_5.configure(text="THE GAME WILL START SOON")
     label_6.configure(text="PLAYER           " + str(player_score) + " : " + str(computer_score)+ "      COMPUTER")
     label_7.configure(text="")
     button_direction.config(text="Perpendicularly", state = NORMAL, relief=RAISED)
     for row in range(5):
          for col in range(5):
               button_display[row][col].configure(bg="white")
     button_display[2][2].configure(bg="black")
     for row in range(10):
          for col in range(10):
               button_player[row][col].configure(bg="white", state = NORMAL, cursor="hand2", relief=SUNKEN)
               button_computer[row][col].configure(bg="white",state = NORMAL, cursor="hand2", relief=RAISED)
                  
#close_window       
def close_window():
    if messagebox.askokcancel("End game", "Do you want to end game?"):
        root.destroy()
#credits info          
def about():
    messagebox.showinfo("About the program", "  Batlle Ships \n\n     v1.0")
#contact info  
def contact():
    messagebox.showinfo("Contact", "If you need help, make any suggestions,\
                        \nplease contact me through this e-mail address: \
                        \n\nkfheigel@gmail.com")
#credits info          
def change_lvl():
    messagebox.showinfo("Changing level", "Level is under development")
    
#hiperlinks opening certain websites     
def hiperlink_1(event):
     webbrowser.open_new(r"https://www.linkedin.com/in/kheigel/")
def hiperlink_2(event):
     webbrowser.open_new(r"https://github.com/klekseusz")
def hiperlink_3(event):
     webbrowser.open_new(r"https://image.ibb.co/gN9ZF6/Business_Card.png")
        
        
#***************************Creating game window********************************
root = Tk()

menu = Menu(root)
root.config(menu = menu)

subMenu = Menu(menu)
menu.add_cascade(label = "Help", menu = subMenu)
subMenu.add_command(label = "About", command = about)
subMenu.add_command(label = "Contact", command = contact)
subMenu.add_command(label = "Credits", command = credits_game)
subMenu.add_command(label = "Reset", command = reset_message_box)
subMenu.add_command(label = "Reset Score", command = reset_score)
subMenu.add_command(label = "Quit", command = close_window)

label_0   = Label(root, borderwidth=2, height = 3, width = 180, relief="groove", text="BATTLESHIPS")
label_1   = Label(root, borderwidth=2, height = 3, width = 62, relief="groove",text="PLAYER MAP")
label_2   = Label(root, borderwidth=2, height = 3, width = 62, relief="groove",text="COMPUTER MAP")
label_3   = Label(root, borderwidth=3, height = 2, width = 30, relief="groove", text="SHIP TO PLACE ON PLAYERS MAP")
label_4   = Label(root, borderwidth=3, height = 2, width = 30, relief="groove", text="4 SHIPS TO GO")
label_5   = Label(root, borderwidth=3, height = 2, width = 30, relief="ridge", text="THE GAME WILL START SOON")
label_6   = Label(root, borderwidth=3, height = 2, width = 30, relief="ridge", text="PLAYER           " + str(player_score) + " : " + str(computer_score)+ "      COMPUTER")
label_7   = Label(root, borderwidth=3, height = 2, width = 30, relief="ridge", text="")
label_8   = Label(root, height = 1, text="Created by:")
label_9   = Label(root, height = 1, text="Krzysztof Heigel", fg="blue", cursor="hand2")
label_10  = Label(root, height = 1, text="GitHub", fg="blue", cursor="hand2")
label_11  = Label(root, height = 1, text="Global Logic", fg="blue", cursor="hand2")


label_0.grid(row=0, columnspan=30)
label_1.grid(row=1, column=1, columnspan=10)
label_2.grid(row=1, column=13, columnspan=10)
label_3.grid(row=5, column=24, columnspan=5)
label_4.grid(row=11, column=24, columnspan=5)
label_5.grid(row=3, column=24, columnspan=5)
label_6.grid(row=1, column=24, columnspan=5)
label_7.grid(row=2, column=24, columnspan=5)
label_8.grid(row=14, column=0, columnspan=2)
label_9.grid(row=14, column=2, columnspan=2)
label_10.grid(row=14, column=4, columnspan=2)
label_11.grid(row=14, column=6, columnspan=2)

label_9.bind("<Button-1>", hiperlink_1)
label_10.bind("<Button-1>", hiperlink_2)
label_11.bind("<Button-1>", hiperlink_3)

#***************************Coordinates********************************
#player coordinates
for coordinates in range(10):
     labelCoHor_player = Label(root, text="%s" %(coordinates+1))
     labelCoHor_player.grid(row=2, column=coordinates+1)
for letters in range(10):
     labelCoVer_player = Label(root, text="%s" %(letter[letters]))
     labelCoVer_player.grid(row=letters+3, column=0)
     
#computer coordinates
for coordinates in range(10):
     labelCoHor_computer = Label(root, text="%s" %(coordinates+1))
     labelCoHor_computer.grid(row=2, column=coordinates+13)
for letters in range(10):
     labelCoVer_computer = Label(root, text="%s" %(letter[letters]))
     labelCoVer_computer.grid(row=letters+3, column=12)
     
#***************************Buttons Grid********************************
button_player=[[0 for row in range(10)] for col in range(10)]
button_computer=[[0 for row in range(10)] for col in range(10)]
button_display=[[0 for row in range(5)] for col in range(5)]
#player map
for row in range(10):
    for col in range(10):
        button_player[row][col] = Button(root, height = 2, width = 4, bg="white",relief=SUNKEN, cursor="hand2", command = lambda row=row, col=col : clicked_player(row, col))
        button_player[row][col].grid(row=row+3, column=col+1, sticky="nsew")
        
#computer map
for row in range(10):
    for col in range(10):
        button_computer[row][col] = Button(root, height = 2, width = 4, bg="white", command = lambda row=row, col=col : clicked_computer(row, col))
        button_computer[row][col].grid(row=row+3, column=col+13, sticky="nsew")
#display
for row in range(5):
    for col in range(5):
        button_display[row][col] = Button(root, height = 2, width = 4, bg="white", relief=SUNKEN)
        button_display[row][col].grid(row=row+6, column=col+24, sticky="nsew")        
button_display[2][2].configure(bg="black")

#function buttons
button_credits      = Button(root, text="Credits", height = 2, width = 10, command = credits_game)
button_reset        = Button(root, text="Reset", height = 2, width = 10, command = reset_message_box)
button_reset_score  = Button(root, text="Reset Score", height = 2, width = 10, command = reset_score)
button_quit         = Button(root, text="Quit", height = 2, width = 10, command = close_window)
button_direction    = Button(root, text="Perpendicularly", height = 2, width = 30, command = change_direction)
button_lvl_1        = Button(root, height = 2, width = 5, font=(None, 6), text="EASY", relief=SUNKEN )
button_lvl_2        = Button(root, height = 2, width = 5, font=(None, 6), text="NORM", command = change_lvl)
button_lvl_3        = Button(root, height = 2, width = 5, font=(None, 6), text="HARD", command = change_lvl)

button_credits.grid(row=13, column=5, columnspan = 2)
button_reset.grid(row=13, column=9, columnspan = 2)
button_reset_score.grid(row=13, column=13, columnspan = 2)
button_quit.grid(row=13, column=17, columnspan = 2)
button_direction.grid(row=12, column=24, columnspan = 5)
button_lvl_1.grid(row=4, column=24, columnspan=1)
button_lvl_2.grid(row=4, column=26, columnspan=1)
button_lvl_3.grid(row=4, column=28, columnspan=1)

#***************************Spacing********************************

root.grid_columnconfigure(0, minsize=20)
root.grid_columnconfigure(11, minsize=20)
root.grid_columnconfigure(23, minsize=40)
root.grid_columnconfigure(29, minsize=40)
root.grid_rowconfigure(13, minsize=60)

root.mainloop()


