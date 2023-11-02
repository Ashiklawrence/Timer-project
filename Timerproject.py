from tkinter import *
import datetime as dt              #Importing all essential modules
import time
import winsound
import threading
root = Tk()                        #assigning tkinter in a variable

cx = False
c1 = False                          #some global declarations for error free code running
c2 = False
c3 = False

def click():

    try:
        global uh, um, c1, c2, c3
        uh = hentry.get()  # getting values from tkinter text box
        um = mentry.get()
        uh = int(uh)
        um = int(um)
        x = dt.datetime.now()  # getting system hour minute and weekday
        h = x.hour
        m = x.minute
        if uh >= h:  # this condition is to check whether the user entry time is smaller than sysytem time
            if um >= m:  # for minute
                global label3
                label3 = Label(root, text="Timer is running...", bg="#2D4356", fg='white')
                label3.grid(row=5, columnspan=2, padx=10, pady=10)
                threading.Thread(target=timer,
                                 daemon=True).start()  # threading the timer function so that the function run seperately reduce system load
                c1 = True  # "daemon = true" is used to stop process while closing window
            else:
                global label6
                label6 = Label(root, text="Enter greater minute", bg="#2D4356", fg='white')
                label6.grid(row=4, columnspan=2)
        else:
            global label7
            label7 = Label(root, text="Enter greater hour", bg="#2D4356", fg='white')
            label7.grid(row=2, columnspan=2)
    except:
        pass

def timer():
    try:
        label6.destroy()                          #this tries to destroy the labels if it is executed or else it passes
        label7.destroy()
    except:
        pass
    global endkey
    endkey = True
    while endkey == True:
        x = dt.datetime.now()  # getting system hour minute
        h = x.hour
        m = x.minute
        if uh == h and um == m:
            global label5
            label5 = Label(root, text="Beep Beep Times Up",bg="#2D4356",fg='red')
            label5.grid(row=9, columnspan=2, padx=10, pady=10)
            label3.destroy()
            for i in range(5):
                winsound.Beep(1500, 500)  # this for is to create beep beep sound
                time.sleep(0.1)                             # this is to create beep space
            break
        time.sleep(1)                                       #this sleep is to run the loop at i second interval to reduce system load
def stop(): #this function is to stop the running timer function loop
    global endkey
    endkey = False
    try:
        label3.destroy()
    except:
        pass
def clear():                                             # this function clears the labels ad clears the entry boxes
    hentry.delete(0,'end')
    mentry.delete(0,'end')
    try:
        label5.destroy()
        label6.destroy()
        label7.destroy()                           # this tries to destroy the labels if it is executed or else it passes
    except:
        pass
root.title('Timer')
root.configure(bg="#2D4356")

label1=Label(root,padx=10,pady=10,text="TIMER",bg="#2D4356",fg='white')
label1.grid(row=0,column=0,columnspan=2)

labelh=Label(root,pady=10,text="Hour:",bg="#2D4356",fg='white')
labelh.grid(row=1,column=0)

hentry=Entry(root,width=20,bg="darkgrey",fg='black')
hentry.grid(row=1,column=1,padx=10,pady=10)

labelh=Label(root,text="Minute:",bg="#2D4356",fg='white')
labelh.grid(row=3,column=0)

mentry=Entry(root,width=20,bg="darkgrey",fg='black')
mentry.grid(row=3,column=1,padx=20,pady=10)

bstart=Button(root,width=10,text="Start",bg="green",fg='white',command=click)
bstart.grid(row=7,padx=10,pady=10,column=1)

bclear=Button(root,width=10,text="Clear",bg="#2D4356",fg='white',command=clear)
bclear.grid(row=7,padx=10,pady=10,column=0)

bend=Button(root,width=10,text="Stop",bg="red",fg='white',command=stop)
bend.grid(row=8,columnspan=2,padx=10,pady=10)

root.mainloop()                                    # this loop is for tkinter window

