from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from datetime import date
from datetime import datetime



win=Tk()

def start_date():
    
    
    def obtain_date(e):
        calendar_button1.config(text=start_date.get_date())
        tp.destroy()
          
        
    tp=Toplevel(win,height=800,width=800)
    tp.title('Start Date')
    
    today_date= date.today()
    
    today_year= today_date.year
    today_month=today_date.month
    today_day=today_date.day
    
    
 
    start_date= Calendar(tp, selectmode='day',showweeknumbers=False,
    showothermonthdays=False, mindate=datetime(today_year,today_month,today_day), maxdate=datetime(2025,12,31))
    start_date.place(x=200,y=200)
    start_date.bind('<<CalendarSelected>>', obtain_date)
    
def end_date():
    
    def obtain_enddate(e):
        calendar_button2.config(text=end_date.get_date())
        tp1.destroy()    
        
        
    tp1=Toplevel(win,height=800,width=800)
    tp1.title('End Date')
    
    today_date= date.today()
    
    today_year= today_date.year
    today_month=today_date.month
    today_day=today_date.day
    
    
 
    end_date= Calendar(tp1, selectmode='day',showweeknumbers=False,
    showothermonthdays=False, mindate=datetime(today_year,today_month,today_day), maxdate=datetime(2025,12,31))
    end_date.place(x=200,y=200)
    
    
    end_date.bind('<<CalendarSelected>>',obtain_enddate)
  
    
def select_room():
    room=1
    adult=1
    child=0
    
      
    def decrease_room():
        nonlocal room
        
        room=int(room_no.cget("text"))
        room=room-1
        
        room_no.config(text=str(room))
        
        text= str(room)+' Rooms, ' + str(adult)+ ' Adult, ' + str(child) + ' Child ' 
        
        room_button.config(text=text)
        if room==1:
            room_dec.config(state='disabled')
        
            room_button.config()
    
    def increase_room():
        nonlocal room
        
        room=int(room_no.cget("text"))
        room=room+1
        room_no.config(text=str(room))
        text= str(room)+' Rooms, ' + str(adult)+ ' Adult, ' + str(child) + ' Child ' 
        
        room_button.config(text=text)
        room_dec.config(state='normal')
        
    def increase_adult():
        
        nonlocal adult
        adult=int(adult_no.cget("text"))
        adult=adult+1
        adult_no.config(text=str(adult))
        
        text= str(room)+' Rooms, ' + str(adult)+ ' Adult, ' + str(child) + ' Child ' 
        
        room_button.config(text=text)
        adult_dec.config(state='normal')
        
    
    def decrease_adult():
        nonlocal adult 
        
        adult=int(adult_no.cget("text"))
        adult=adult-1
        
        adult_no.config(text=str(adult))
        text= str(room)+' Rooms, ' + str(adult)+ ' Adult, ' + str(child) + ' Child ' 
        
        room_button.config(text=text)
        if adult==1:
            adult_dec.config(state='disabled')
        
    def decrease_child():
        nonlocal child
        child=int(child_no.cget("text"))
        child=child-1
        
        child_no.config(text=str(child))
        
        text= str(room)+' Rooms, ' + str(adult)+ ' Adult, ' + str(child) + ' Child ' 
        
        room_button.config(text=text)
        if child==0:
            child_dec.config(state='disabled')
    
    
    def increase_child():
        nonlocal child
        child=int(child_no.cget("text"))
        child=child+1
        child_no.config(text=str(child))
        
        text= str(room)+' Rooms, ' + str(adult)+ ' Adult, ' + str(child) + ' Child ' 
        
        room_button.config(text=text)
        child_dec.config(state='normal')
    
    
    
    tp2=Toplevel(win,height=400,width=400)
    tp2.title('Select Rooms')
   
    
   #  Room details
   
    label1=Label(tp2,text='Room',font=("Arial",15))
    label1.place(x=10,y=10)    
    
    room_dec=Button(tp2,text= '-',command=decrease_room,font=("Arial",15),state='disabled')
    room_dec.place(x=150,y=10)

    room_no = Label(tp2,text='1',font=("Arial",15))
    room_no.place(x=200,y=10)


    room_inc=Button(tp2,text= '+',command=increase_room,font=("Arial",15))
    room_inc.place(x=250,y=10)

    
   #  Adult details

    label2=Label(tp2,text='Adults',font=("Arial",15))
    label2.place(x=10,y=100)    
 
    adult_dec=Button(tp2,text= '-',command=decrease_adult,font=("Arial",15),state='disabled')
    adult_dec.place(x=150,y=100)

    adult_no = Label(tp2,text='1',font=("Arial",15))
    adult_no.place(x=200,y=100)

    adult_inc=Button(tp2,text= '+',command=increase_adult,font=("Arial",15))
    adult_inc.place(x=250,y=100)

    #  Child details

    label3=Label(tp2,text='Children',font=("Arial",15))
    label3.place(x=10,y=200)    
  
    child_dec=Button(tp2,text= '-',command=decrease_child,font=("Arial",15),state='disabled')
    child_dec.place(x=150,y=200)

    child_no = Label(tp2,text='0',font=("Arial",15))
    child_no.place(x=200,y=200)
    child_inc=Button(tp2,text= '+',command=increase_child,font=("Arial",15))
    child_inc.place(x=250,y=200)
    
    

title_label=Label(win,text="Hotel Booking Point",font=("Arial Bold",30),fg='blue')
title_label.place(x=500,y=50)

n=StringVar()
destination= ttk.Combobox(win, width=125, height=20,textvariable=n)
destination['values']=('Enter a destination','Bangalore','Hyderabad','Chennai','Lucknow','Pune','Mumbai')

destination.place(x=350,y=150)
destination.current(0)

calendar_button1=Button(win,width=20,bg='white', fg='blue',height=5,text='Start Date',command=start_date)
calendar_button1.place(x=500,y=200)

calendar_button2=Button(win,width=20,height=5,fg='blue',bg='white',text='End Date',command=end_date)
calendar_button2.place(x=800,y=200)

room_button=Button(win,width=30,height=3,fg='blue',bg='white',text=' 1 adult , 1 room , 0 child ',command=select_room)
room_button.place(x=600,y=300)

search_btn=Button(win,width=20,height=3,bg='blue',text='SEARCH',fg='white')
search_btn.place(x=650,y=400)

win.mainloop()
