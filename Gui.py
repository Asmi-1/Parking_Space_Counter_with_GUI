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
slot_empty = slot_empty.resize((80, 90), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(slot_empty)
slot_filled = Image.open('red.png')
slot_filled = slot_filled.resize((80, 90), Image.ANTIALIAS)
my_img2 = ImageTk.PhotoImage(slot_filled)
colour="yellow" 
#
count=0
bt=[]
spacesEmpty={1,6,25,63}

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
          temp=count +1
          if temp in spacesEmpty :
               bt.append(tkinter.Button(window, text="Slot "+str(count+1), image=my_img, compound='top', borderwidth=3, relief="solid"))
               bt[count].grid(column=j, row=i)  
               count=count+1
          else :
               bt.append(tkinter.Button(window, text="Slot "+str(count+1), image=my_img2, compound='top', borderwidth=3, relief="solid"))
               bt[count].grid(column=j, row=i)  
               count=count+1
          






window.mainloop()                                                                                                                                                                

