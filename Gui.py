from distutils.command.sdist import sdist
import tkinter
import tkinter.messagebox
from PIL import ImageTk, Image
print("This is SS MP")

# Creating window object
window = tkinter.Tk()
window.title("Parking lot")
label = tkinter.Label(window, text="This is the parking lot")
l1 = tkinter.Label(window, text="Parking Lot")
window.geometry('1000x900')
window.configure(bg='gray')
l1.grid(column=0, row=0)




# Importing Images
slot_empty = Image.open('green.png')
slot_empty = slot_empty.resize((100, 130), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(slot_empty)
slot_filled = Image.open('red.png')
slot_filled = slot_filled.resize((100, 130), Image.ANTIALIAS)
my_img2 = ImageTk.PhotoImage(slot_filled)

colour="yellow" 
# Creating 5 consecutive slots
##
count=0
bt=[]
for i in range(2,10):
     if i==4 :
          l3 = tkinter.Label(window, bg="gray", text="Road")
          l3.grid(row=4) 
          continue;
     if i==7 :
          l3 = tkinter.Label(window, bg="gray", text="Road")
          l3.grid(row=7)  
          continue; 
          

     for j in range(1,13):
          bt.append(tkinter.Button(window, text="Slot "+str(count+1), image=my_img, compound='top', borderwidth=3, relief="solid"))
          bt[count].grid(column=j, row=i)  
          count=count+1
##




# Creating a 3 row wide road
#l2 = tkinter.Label(window, bg="gray", text="\t")
#l2.grid(row=3)
# l3 = tkinter.Label(window, bg="gray", text="Road")
# l3.grid(row=4)
#l4 = tkinter.Label(window, bg="gray", text="\t")
#l4.grid(row=5)

# bt1 = tkinter.Button(window, text="Slot 1", image=my_img, compound='top', borderwidth=3, relief="solid")
# bt1.grid(column=1, row=2)
# bt2 = tkinter.Button(window, text="Slot 2", image=my_img,compound='top')
# bt2.grid(column=2, row=2)
# bt3 = tkinter.Button(window, text="Slot 3", image=my_img,compound='top')
# bt3.grid(column=3, row=2)
# bt4 = tkinter.Button(window, text="Slot 4", image=my_img,compound='top')
# bt4.grid(column=4, row=2)
# bt5 = tkinter.Button(window, text="Slot 5", image=my_img,compound='top')
# bt5.grid(column=5, row=2)
# bt6 = tkinter.Button(window, text="Slot 6", image=my_img,compound='top')
# bt6.grid(column=6, row=2)
# bt7 = tkinter.Button(window, text="Slot 7", image=my_img,compound='top')
# bt7.grid(column=7, row=2)
# bt8 = tkinter.Button(window, text="Slot 8", image=my_img,compound='top')
# bt8.grid(column=8, row=2)
# bt9 = tkinter.Button(window, text="Slot 9", image=my_img,compound='top')
# bt9.grid(column=9, row=2)
# bt10 = tkinter.Button(window, text="Slot 10", image=my_img,compound='top')
# bt10.grid(column=10, row=2)
# bt11 = tkinter.Button(window, text="Slot 11", image=my_img,compound='top')
# bt11.grid(column=11, row=2)
# bt12 = tkinter.Button(window, text="Slot 12", image=my_img,compound='top')
# bt12.grid(column=12, row=2)
# bt13 = tkinter.Button(window, text="Slot 13", image=my_img, compound='top')
# bt13.grid(column=1, row=3)
# bt14 = tkinter.Button(window, text="Slot 14", image=my_img,compound='top')
# bt14.grid(column=2, row=3)
# bt15 = tkinter.Button(window, text="Slot 15", image=my_img,compound='top')
# bt15.grid(column=3, row=3)
# bt16 = tkinter.Button(window, text="Slot 16", image=my_img,compound='top')
# bt16.grid(column=4, row=3)
# bt17 = tkinter.Button(window, text="Slot 17", image=my_img,compound='top')
# bt17.grid(column=5, row=3)
# bt18 = tkinter.Button(window, text="Slot 18", image=my_img,compound='top')
# bt18.grid(column=6, row=3)
# bt19 = tkinter.Button(window, text="Slot 19", image=my_img,compound='top')
# bt19.grid(column=7, row=3)
# bt20 = tkinter.Button(window, text="Slot 20", image=my_img,compound='top')
# bt20.grid(column=8, row=3)
# bt21 = tkinter.Button(window, text="Slot 21", image=my_img,compound='top')
# bt21.grid(column=9, row=3)
# bt22 = tkinter.Button(window, text="Slot 22", image=my_img,compound='top')
# bt22.grid(column=10, row=3)
# bt23 = tkinter.Button(window, text="Slot 23", image=my_img,compound='top')
# bt23.grid(column=11, row=3)
# bt24 = tkinter.Button(window, text="Slot 24", image=my_img,compound='top')
# bt24.grid(column=12, row=3)

# Creating 5 consecutive slots
# bt25 = tkinter.Button(window, text="Slot 25", image=my_img,compound='top')
# bt25.grid(column=1, row=5)
# bt26 = tkinter.Button(window, text="Slot 26", image=my_img,compound='top')
# bt26.grid(column=2, row=5)
# bt27 = tkinter.Button(window, text="Slot 27", image=my_img,compound='top')
# bt27.grid(column=3, row=5)
# bt28 = tkinter.Button(window, text="Slot 28", image=my_img,compound='top')
# bt28.grid(column=4, row=5)
# bt29 = tkinter.Button(window, text="Slot 29", image=my_img,compound='top')
# bt29.grid(column=5, row=5)
# bt30 = tkinter.Button(window, text="Slot 30", image=my_img,compound='top')
# bt30.grid(column=6, row=5)
# bt31 = tkinter.Button(window, text="Slot 31", image=my_img,compound='top')
# bt31.grid(column=7, row=5)
# bt32 = tkinter.Button(window, text="Slot 32", image=my_img,compound='top')
# bt32.grid(column=8, row=5)
# bt33 = tkinter.Button(window, text="Slot 33", image=my_img,compound='top')
# bt33.grid(column=9, row=5)
# bt34 = tkinter.Button(window, text="Slot 34", image=my_img,compound='top')
# bt34.grid(column=10, row=5)
# bt35 = tkinter.Button(window, text="Slot 35", image=my_img,compound='top')
# bt35.grid(column=11, row=5)
# bt36 = tkinter.Button(window, text="Slot 36", image=my_img,compound='top')
# bt36.grid(column=12, row=5)

# Creating 5 consecutive slots
# bt37 = tkinter.Button(window, text="Slot 37", image=my_img,compound='top')
# bt37.grid(column=1, row=6)
# bt38 = tkinter.Button(window, text="Slot 38", image=my_img,compound='top')
# bt38.grid(column=2, row=6)
# bt39 = tkinter.Button(window, text="Slot 39", image=my_img,compound='top')
# bt39.grid(column=3, row=6)
# bt40 = tkinter.Button(window, text="Slot 40", image=my_img,compound='top')
# bt40.grid(column=4, row=6)
# bt41 = tkinter.Button(window, text="Slot 41", image=my_img,compound='top')
# bt41.grid(column=5, row=6)
# bt42 = tkinter.Button(window, text="Slot 42", image=my_img,compound='top')
# bt42.grid(column=6, row=6)
# bt43 = tkinter.Button(window, text="Slot 43", image=my_img,compound='top')
# bt43.grid(column=7, row=6)
# bt44 = tkinter.Button(window, text="Slot 44", image=my_img,compound='top')
# bt44.grid(column=8, row=6)
# bt45 = tkinter.Button(window, text="Slot 45", image=my_img,compound='top')
# bt45.grid(column=9, row=6)
# bt46 = tkinter.Button(window, text="Slot 46", image=my_img,compound='top')
# bt46.grid(column=10, row=6)
# bt47 = tkinter.Button(window, text="Slot 47", image=my_img,compound='top')
# bt47.grid(column=11, row=6)
# bt48 = tkinter.Button(window, text="Slot 48", image=my_img,compound='top')
# bt48.grid(column=12, row=6)


# Creating a 3 row wide road
#l2 = tkinter.Label(window, bg="gray", text="\t")
#l2.grid(row=8)
# l3 = tkinter.Label(window, bg="gray", text="Road")
# l3.grid(row=7)
#l4 = tkinter.Label(window, bg="gray", text="\t")
#l4.grid(row=10)

# Creating 5 consecutive slots
# bt49 = tkinter.Button(window, text="Slot=49", image=my_img,compound='top')
# bt49.grid(column=1, row=8)
# bt50 = tkinter.Button(window, text="Slot=50", image=my_img,compound='top')
# bt50.grid(column=2, row=8)
# bt51 = tkinter.Button(window, text="Slot 51", image=my_img,compound='top')
# bt51.grid(column=3, row=8)
# bt52 = tkinter.Button(window, text="Slot 52", image=my_img,compound='top')
# bt52.grid(column=4, row=8)
# bt53 = tkinter.Button(window, text="Slot 53", image=my_img,compound='top')
# bt53.grid(column=5, row=8)
# bt54 = tkinter.Button(window, text="Slot 54", image=my_img,compound='top')
# bt54.grid(column=6, row=8)
# bt55 = tkinter.Button(window, text="Slot 55", image=my_img,compound='top')
# bt55.grid(column=7, row=8)
# bt56 = tkinter.Button(window, text="Slot 56", image=my_img,compound='top')
# bt56.grid(column=8, row=8)
# bt57 = tkinter.Button(window, text="Slot 57", image=my_img,compound='top')
# bt57.grid(column=9, row=8)
# bt58 = tkinter.Button(window, text="Slot 58", image=my_img,compound='top')
# bt58.grid(column=10, row=8)
# bt59 = tkinter.Button(window, text="Slot 59", image=my_img,compound='top')
# bt59.grid(column=11, row=8)
# bt60 = tkinter.Button(window, text="Slot 60", image=my_img,compound='top')
# bt60.grid(column=12, row=8)
# bt61 = tkinter.Button(window, text="Slot 61", image=my_img, compound='top')
# bt61.grid(column=1, row=9)
# bt62 = tkinter.Button(window, text="Slot 62", image=my_img,compound='top')
# bt62.grid(column=2, row=9)
# bt63 = tkinter.Button(window, text="Slot 63", image=my_img,compound='top')
# bt63.grid(column=3, row=9)
# bt64 = tkinter.Button(window, text="Slot 64", image=my_img,compound='top')
# bt64.grid(column=4, row=9)
# bt65 = tkinter.Button(window, text="Slot 65", image=my_img,compound='top')
# bt65.grid(column=5, row=9)
# bt66 = tkinter.Button(window, text="Slot 66", image=my_img,compound='top')
# bt66.grid(column=6, row=9)
# bt67 = tkinter.Button(window, text="Slot 67", image=my_img,compound='top')
# bt67.grid(column=7, row=9)
# bt68 = tkinter.Button(window, text="Slot 68", image=my_img,compound='top')
# bt68.grid(column=8, row=9)
# bt69 = tkinter.Button(window, text="Slot 69", image=my_img,compound='top')
# bt69.grid(column=9, row=9)




#dkt
# clear


# directions=["slot1 on right after entry",
# "slot2 on right after entry","slot3 on right after entry","slot4 on right after entry","slot5 on right after entry",
# "slot6 on left after entry","slot7 on left after entry","slot8 on left after entry","slot9 on left after entry"
# ,"slot10 on left after entry","slot11 on left after taking two left turns and entering into 2nd lane",
# "slot12 on left after taking two left turns and entering into 2nd lane","slot13 on left after taking two left turns and entering into 2nd lane",
# "slot14 on left after taking two left turns and entering into 2nd lane","slot15 on left after taking two left turns and entering into 2nd lane",
# "slot16 on right after taking two left turns and entering into 2nd lane","slot17 on right after taking two left turns and entering into 2nd lane",
# "slot18 on right after taking two left turns and entering into 2nd lane","slot19 on right after taking two left turns and entering into 2nd lane",
# "slot20 on right after taking two left turns and entering into 2nd lane"]





# def opt_1(lst):
#     temp=min(lst)
#     tkinter.messagebox.showinfo("Welcome to the CARPARK","{} slot is assigned to you, These are the directions :{}".format(temp+1,directions[temp]))
#     dkt[temp]['image']=my_img2
#     lst.remove(temp)
    
    

# def opt_2(n,lst):
#   tkinter.messagebox.showinfo("Welcome to the CARPARK", "{} number of cars are parked, {} slots are free".format(n,len(lst)))

  
# def opt_3(slot_remove, car_slot_empty):
#     dkt[slot_remove-1]['image']=my_img
#     car_slot_empty.append(slot_remove-1)
#     car_slot_empty.sort()

#Console Code
# print("Welcome to CARPARK\n")
# n = 0 #Number of Cars 
# car_slot_empty=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
# while (True):
#     print("Enter 1 to find a parking in the CARPARK\n")
#     print("Enter 2 to display status of CARPARK\n")
#     print("Enter 3 to remove your car\n")
#     print("Enter 4 To Exit\n")
#     print("Enter Your Option:")
#     x = int(input())
#     if (x == 1):
#         if(n<20):
#             n+=1
#             opt_1(car_slot_empty)
#         else:
#             tkinter.messagebox.showerror("Parking Allotment.",  "The garage is full, Please try later")
#     elif(x == 2):
#         opt_2(n,car_slot_empty)
#     elif (x == 3):
#         if(n>0):
#           n-=1
#           print("Enter the slot number of the car you want to remove:")
#           slot_remove=int(input())
#           if(slot_remove-1 in car_slot_empty):
#               tkinter.messagebox.showinfo("Parking Allotment","Slot {} is empty".format(slot_remove))
#           else:
#             opt_3(slot_remove, car_slot_empty)
#         else:
#           tkinter.messagebox.showerror("Parking Allotment.",  "There is no car in the garage")
#     elif (x == 4):
#       print("Goodbye\n")
#       break
#     else:
#       print("Enter An Valid Option")
# Main loop to keep the window open as long as user wants
window.mainloop()                                                                                                                                                                

