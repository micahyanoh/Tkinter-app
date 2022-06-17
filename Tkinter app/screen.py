import tkinter as tk

#declaring background color
bg_color='#3d6466'

def clear_widget(frame):
    #select all the widgets and delete them
    for widget in frame.winfo_children():
        widget.destroy()

def load_frame1(): 
    #destroy widgets and avoid crowding
    clear_widget(frame2)
    clear_widget(frame3)
    #stack widgets above existing ones
    frame1.tkraise()
    #prevet widgets from modifying screen
    frame1.pack_propagate(False)
    tk.Label(
    frame1,
    text='Do you want to exolore this App?',
    bg='#28393a',
    fg='white'
            ).pack(pady=20)
    tk.Button(
    frame1,text='WIDGETS',
    relief='flat',
    bg='#28393a',
    fg='white',
    command=lambda:load_frame2()
        ).pack(pady=20)

def load_frame2():
    #destroy widgets and avoid crowding
    clear_widget(frame1)
    clear_widget(frame3)
    #stack widgets above existing ones
    frame2.tkraise()
    #prevet widgets from modifying screen
    frame2.pack_propagate(False) 
    tk.Label(
        frame2,text='Hello world!',
        height='30',width='50',
        bg=bg_color,fg='black',
        cursor='hand2'
            ).pack(pady=25)
    tk.Button(
        frame2,text='BACK',
        bg='#28393a',
        fg='white',
        relief='flat',
        command=lambda:load_frame1()
            ).pack(side=tk.LEFT,padx=20,pady=20)
    tk.Button(
        frame2,text='NEXT',
        bg='#28393a',
        fg='white',
        relief='flat',command=lambda:load_frame3()
             ).pack(side=tk.RIGHT,padx=20,pady=20)
def load_frame3(): 
        #destroy widgets and avoid crowding
        clear_widget(frame1)
        clear_widget(frame2)
        #stack widgets above existing ones
        frame3.tkraise()
        #prevet widgets from modifying screen
        frame3.pack_propagate(False)
        tk.Button(
        frame3,text='HOME',
        relief='flat',
        bg='#28393a',
        fg='white',
        border='3px',
        command=lambda:load_frame1()
                 ).pack(side=tk.BOTTOM,pady=20)
        tk.Label(
        frame3,text='Hello world',
        height='30',width='50',
        bg=bg_color,fg='white',
        cursor='hand2'
                ).pack(pady=25)
   
app=tk.Tk()
app.title('My screen')
#app.eval('tk::PlaceWindow . Center')
app.resizable(0,0)
app.config(bg=bg_color)
#exiting shortcuts,press Q or q to exit
app.bind('<q>',exit)
app.bind('<Q>',exit)

frame1=tk.Frame(app,width=500,height=600,bg=bg_color) 
frame2=tk.Frame(app,width=500,height=600,bg='pink')
frame3=tk.Frame(app,width=500,height=600,bg='black')
for frame in (frame1,frame2,frame3):
    frame.grid(row=0,column=0)

load_frame1()


app.mainloop()