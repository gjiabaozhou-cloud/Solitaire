#Solitaire

import tkinter as tk
root=tk.Tk()
root.config(bg='green')
root.geometry("400x500")
#from dataclasses import dataclass
#from typing import List
import random


#RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
#SUITS = ['♠','♥','♦','♣']



deck_list=['HA','H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK',
      'DA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK',
      'CA','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK',
      'SA','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK']
#Pairings
#H can pair with C or S not D
#D can pair with D or S not H
#C can pair with H or D not S
#S can pair with H or D not C

random.shuffle(deck_list)
#print(deck_list)
red=['HA','H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK',
     'DA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK']
# tk.Button(root, text='H1')
card_dict = {}
button_dict = {}
for i in deck_list:
    card_dict[i] = i
    button_dict[i] = tk.Button(root, text=i, height=3, width=3)
    if i in red:
        button_dict[i].config(fg='red')
        
#print("card dictionary", card_dict)
print("buttons", button_dict)
L1=[deck_list[0]]
L2=list(deck_list[1:3])
L3=list(deck_list[3:6])
L4=list(deck_list[6:10])
L5=list(deck_list[10:15])
L6=list(deck_list[15:21])
L7=list(deck_list[21:28])

Ldeck=list(deck_list[28:52])
print(L1, L2, L3, L4, L5, L6, L7)

print(Ldeck)

#If card is last of list, then displayed
#If card displayed (True), then continued displayed
'''
L1[-1]=True
L2[-1]=True
L3[-1]=True
L4[-1]=True
L5[-1]=True
L6[-1]=True
L7[-1]=True
'''



print(L1[-1])
button_deck=tk.Button(root,text='Deck')
button_deck.grid(row=0,column=0)
#line 1
(button_dict[L1[-1]]).grid(row=2,column=0,sticky='nsew')
for i in range(len(L2)):
    if i!=1:
        button_dict[L2[i]].config(fg='gray',bg='gray')
    button_dict[L2[i]].grid(row=i+2,column=1,sticky='nsew')
for i in range(len(L3)):
    if i!=2:
        button_dict[L3[i]].config(fg='gray',bg='gray')
    button_dict[L3[i]].grid(row=i+2,column=2,sticky='nsew')
for i in range(len(L4)):
    if i!=3:
        button_dict[L4[i]].config(fg='gray',bg='gray')
    button_dict[L4[i]].grid(row=i+2,column=3,sticky='nsew')
for i in range(len(L5)):
    if i!=4:
        button_dict[L5[i]].config(fg='gray',bg='gray')
    button_dict[L5[i]].grid(row=i+2,column=4,sticky='nsew')
for i in range(len(L6)):
    if i!=5:
        button_dict[L6[i]].config(fg='gray',bg='gray')
    button_dict[L6[i]].grid(row=i+2,column=5,sticky='nsew')
for i in range(len(L7)):
    if i!=6:
        button_dict[L7[i]].config(fg='gray',bg='gray')
    button_dict[L7[i]].grid(row=i+2,column=6,sticky='nsew')


frameH = tk.Frame(root, width=25, height=25, bg="darkgray")
frameC = tk.Frame(root, width=25, height=25, bg="darkgray")
frameS = tk.Frame(root, width=25, height=25, bg="darkgray")
frameD = tk.Frame(root, width=25, height=25, bg="darkgray")

frameH.grid(row=0,column=3,padx=1,pady=1)
frameC.grid(row=0,column=4,padx=1,pady=1)
frameS.grid(row=0,column=5,padx=1,pady=1)
frameD.grid(row=0,column=6,padx=1,pady=1)

# Configure column 0 to have a minimum width of 100 pixels
#root.columnconfigure(0,minsize=50) #

# Configure row 1 to have a minimum height of 50 pixels
#root.rowconfigure(0,minsize=50)

#Dragging
#global start_x, start_y
#start_x=0
#start_y=0
def start_drag(event):
    global drag_widgets
    drag_widgets=[]
    widget=event.widget
    global old_pos
    #global start_x,start_y
    # Store initial click offset
    event.widget.start_x = event.x
    event.widget.start_y = event.y
    #start_x=event.x
    #start_y=event.y
    #print(start_x,start_y)
    old_pos=widget.grid_info()
    col=old_pos['column']
    row=old_pos['row']
    print("column",columns[col])
    if widget in show_deck:
        drag_widgets=widget
    else:
        for i in columns[col]:
            btn=button_dict[i]
            info=btn.grid_info()
            #print(i, btn, info)
            if 'row' in info and info['row']>=row:
                #print(i, info)
                drag_widgets.append(btn)
    print('drag_widgets',drag_widgets)
    
def do_drag(event):
    # Calculate new position and update with place()
    x = event.widget.winfo_x() - event.widget.start_x + event.x
    y = event.widget.winfo_y() - event.widget.start_y + event.y
    i=0
    for w in drag_widgets:
        w.place(x=x,y=y+i)
        print('i',i)
        i+=1 
        
    #event.widget.place(x=x, y=y)
    
#def move_to_target(event):
    # If in target area, move to final target position (using x.event and y.event cords)
    
def card_values(text):
    value=0
    if "A" in text:
        value=1
    if "J" in text:
        value=11
    elif "Q" in text:
        value=12
    elif "K" in text:
        value=13
    else:
        for i in range(2,11):
            if str(i) in text:
                value=i
    return value

def item_value(text,text2):
    if "H" in text:
        if ("C" in text2) or ("S" in text2):
            return True
        else:
            return False
    elif "D" in text:
        if ("C" in text2) or ("S" in text2):
            return True
        else:
            return False
    elif "C" in text:
        if ("H" in text2) or ("D" in text2):
            return True
        else:
            return False
    elif "S" in text:
        if ("H" in text2) or ("D" in text2):
            return True
        else:
            return False
        
        
def check_if_can_snap(text1,text2):
    if card_values(text2)-card_values(text1)==1:
        if item_value(text1,text2)==True:
            return True
        else:
            return False
    else:
        return False
                
def stop_drag(event):
    widget = event.widget

    # Force position update
    root.update_idletasks()

    x = widget.winfo_x()

    closest_col = None
    min_dist = float('inf')

    # Find closest column based on x position
    for col in range(7):
        slaves = [w for w in root.grid_slaves(column=col) if isinstance(w, tk.Button)]
        if not slaves:
            continue

        ref = slaves[0]  # any widget in that column
        col_x = ref.winfo_x()
        main_ref=slaves[-1]

        dist = abs(x - col_x)
        if dist < min_dist:
            min_dist = dist
            closest_col = col
            count=0
            for i in slaves:
                count+=1

    if closest_col is not None:
    

        # Find next available row in that column
        #col_widgets = root.grid_slaves(column=closest_col)
        #new_row = max([w.grid_info()['row'] for w in col_widgets], default=1) +1
        new_row = len(columns[closest_col]) + 2
        #if closest_col!=1:
        #    new_row+=1
        text1=widget.cget('text')
        if columns[closest_col]==[]:
            if "K" in text1:
                widget.place_forget()
                widget.grid(row=new_row, column=closest_col)
                columns[closest_col].append(widget.cget("text"))
                if widget.cget("text") in columns[closet_col]:
                    col.remove(widget.cget("text"))
        try:
            text2 = columns[closest_col][-1]
            print(text2)
            truth_value=check_if_can_snap(text1,text2)
            print('truth_value',truth_value)
            if truth_value==True:
                for col in columns:
                    if widget.cget("text") in columns[closest_col]:
                        col.remove(widget.cget("text"))
                        
                        if col != []:
                            old_row=old_pos['row']
                            old_col=old_pos['column']
                            get_position()
                            card_above=position_map.get((old_row-1,old_col))
                            print('act_card_above',col[-1])
                            button_dict[col[-1]].config(fg='black',bg='white')
                            if card_above in red:
                                button_dict[col[-1]].config(fg='red')
                            #button_dict[col[-1]].grid(row=old_row-1,column=old_col,sticky='nsew')
                            
                
                widget.place_forget()
                widget.grid(row=new_row, column=closest_col)
                columns[closest_col].append(widget.cget("text"))
                print(old_pos)
                old_row=old_pos['row']
                old_col=old_pos['column']
                get_position()
                card_above=position_map.get((old_row-1,old_col))
                print('card above', card_above)
                
                if card_above != None:
                    button_dict[card_above].grid(row=old_row-1,column=old_col,sticky='nsew', width=2,height=3)
            else:
                widget.grid(**old_pos)
                #widget.place_forget()
                #print(start_x,start_y)
                #widget.grid(row=start_x,column=start_y)
        except RuntimeError:
            widget.grid(**old_pos)
            #widget.place_forget()
            #widget.grid(row=start_x,column=start_y)
        show_bottom_card()
        make_buttons_red(widget)
    
        
def drag_all_below(event):
    pass

def show_card_above(event):
    pass
show_deck=[]
def show_deck_card(event):
    global show_deck
    show_deck.append(Ldeck[-1])
    Ldeck.pop()
    btn=tk.Button(root,text=show_deck, height=3,width=2)
    if show_deck in red:
        btn.config(fg='red')
    btn.grid(row=0,column=1,sticky='nsew')
    btn.lift()
    btn.bind('<Button-1>',start_drag)
    btn.bind('<B1-Motion>',do_drag)
    btn.bind('<ButtonRelease-1>',stop_drag)
    
    
def make_buttons_red(btn):
    text=btn.cget('text')
    btn.config(fg='black')
    if text in red:
        btn.config(fg='red')
    
old_pos={}
position_map={}
'''
print('button_dict', list(button_dict.values()))
for i in list(button_dict.values()):
    if i.grid_info:
        pos=i.grid_info()
        row=pos['row']
        col=pos['column']
'''
def get_position():
    for widget in button_dict.values():
        pos = widget.grid_info()

        # only process widgets that actually have grid info
        if 'row' in pos and 'column' in pos:
            row = pos['row']
            col = pos['column']

            text = widget.cget("text")
            position_map[text] = (row, col)
            
def show_bottom_card():
    for line in columns:
        if len(line)!=0:
            button_dict[line[-1]].bind("<Button-1>", start_drag)
            button_dict[line[-1]].bind("<B1-Motion>", do_drag)
            button_dict[line[-1]].bind("<ButtonRelease-1>", stop_drag)
        
#Binding events
button_deck.bind("<Button-1>",show_deck_card)
columns=[L1,L2,L3,L4,L5,L6,L7]
for line in columns:
    button_dict[line[-1]].bind("<Button-1>", start_drag)
    button_dict[line[-1]].bind("<B1-Motion>", do_drag)
    button_dict[line[-1]].bind("<ButtonRelease-1>", stop_drag)


root.mainloop()


