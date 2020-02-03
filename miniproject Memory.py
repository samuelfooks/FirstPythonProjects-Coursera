# implementation of card game - Memory

import simplegui
import random

card_list1=[0,1,2,3,4,5,6,7]
card_list2=[0,1,2,3,4,5,6,7]

card_list=card_list1+card_list2

exposed_list1=[False,False,False,False,False,False,False,False]
exposed_list2=[False,False,False,False,False,False,False,False]
exposed_list=exposed_list1+exposed_list2

clicked_index1=0
clicked_index2=0

turns=0

found_pairs=0

random.shuffle(card_list)

# helper function to initialize globals
def new_game():
    global card_list
    global state
    global turns
    global exposed_list
    global found_pairs
    state=0
    turns=0
    for exposed_index in range(len(exposed_list)):
        exposed_list[exposed_index]=False
    
    found_pairs=0

     
# define event handlers

    
def mouseclick(pos):
    # add game state logic here
    global exposed_list
    global card_list
    global exposed_pos
    global state
    global card_index
    global clicked_index1
    global clicked_index2
    global found_pairs
    global turns
    
    
    for exposed_index in range(len(exposed_list)):
        exposed_pos=(50*exposed_index)+25
        
        if pos[0] <= exposed_pos+24 and pos[0]>=exposed_pos-24 and pos[1]>=0 and pos[1]<=100 and exposed_list[exposed_index]==False:
            exposed_list[exposed_index]=True
            if state == 0:
                clicked_index1=exposed_index
               
                state = 1
               
            elif state == 1:
                turns+=1
                
                clicked_index2=exposed_index
               
                state = 2
                
                
              
           
                
            else:
                if exposed_list[clicked_index1]==True and exposed_list[clicked_index2]==True and card_list[clicked_index1]==card_list[clicked_index2]:
                
                    found_pairs+=1
                 
               
                else: 
                    exposed_list[clicked_index2]=False
                    exposed_list[clicked_index1]=False
                    
                    
                clicked_index1=exposed_index
                state=1
            

           
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global state
    global turns
   
    for card_index in range(len(card_list)):
        card_pos=(50*card_index)+25
        canvas.draw_text(str(card_list[card_index]),[card_pos,40], 36, "red")
        
        
    
    for exposed_index in range(len(exposed_list)):
        if exposed_list[exposed_index] == False:
            exposed_pos=(50* exposed_index)+25
            canvas.draw_line([exposed_pos,0],[exposed_pos,100],48, "green")
              
    for exposed in range(len(exposed_list)):
        if exposed_list.count(True)==16:
            canvas.draw_text("You win! Click Reset", [50,80], 36, "yellow")
    
    label1.set_text("Turns= "+ str(turns))
    label2.set_text("Found Pairs = "+ str(found_pairs) )
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label1 = frame.add_label("Turns ")
label2= frame.add_label("pairs found")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric