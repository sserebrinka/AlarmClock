import datetime
import time
import pyglet
from tkinter import *
import tkinter
from PIL import Image, ImageTk


#Окно
window = Tk()
window.title('Alarm clock')
window.geometry('1000x1000')

frame = tkinter.Frame(window)
frame.grid()

#Фоновое изображение

canvas = tkinter.Canvas(window, height=1000, width=1000)
image = Image.open("alarmclock.png")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.grid(row=0, column=0)


#Дата сегодня
time_now = datetime.datetime.now()
time_txt = 'DATE\n' + str(time_now)[:10]
time_txt_0 = canvas.create_text(100, 50, text=time_txt,
                            font=("Arial Rounded MT Bold", 20), fill='#999999',
                            justify=CENTER, anchor=CENTER)

#Время сегодня
def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    canvas.itemconfig(time_1, text='TIME\n' + hour + ':' + minute + ':' + second)
    canvas.after(1000, clock)
def Alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M")
        cur_date = actual_time.strftime("%d/%m")
        msg = "Current Time: " + str(cur_time)
        print(msg)
        if cur_time == set_alarm_timer:
            music.play()
            break
def set_alarm_timer():
    alarm_set_time = f"{hour_1.get()}:{minutes_1.get()}"
    Alarm(alarm_set_time)

def clicked():
    label1["text"] = hour_1.get()
    label2["text"] = minutes_1.get()


time_0 = 'TIME'
time_1 = canvas.create_text(100, 150, text=time_0,
                            font=("Arial Rounded MT Bold", 20), fill='#999999',
                            justify=CENTER, anchor=CENTER)

clock()

music = pyglet.resource.media('alarm.mp3')

hour_1 = Entry(window, width=100, font=("Arial Rounded MT Bold", 50))
hour_1.place(x=200, y=600, width=100, height=100)
minutes_1 = Entry(window, width=100, font=("Arial Rounded MT Bold", 50))
minutes_1.place(x=350, y=600, width=100, height=100)

btn1 = Button(window, text='OK', fg='#999999', font=('Arial Rounded MT Bold', 30), command=clicked)
btn1.place(x=200, y=700, width=250, height=50)

label1 = Label(font=('Arial Rounded MT Bold', 50), foreground='#999999', background='white')
label1.place(x=600, y=610, width=100, height=100)

label2 = Label(font=('Arial Rounded MT Bold', 50), foreground='#999999', background='white')
label2.place(x=700, y=610, width=100, height=100)

dvoetoch1 = ':'
dvoetoch11 = canvas.create_text(323, 650, text=dvoetoch1,
                            font=("Arial Rounded MT Bold", 50), fill='#999999',
                            justify=CENTER, anchor=CENTER)

text_clock = 'THE ALARM CLOCK IS SET TO:'
text_clock1 = canvas.create_text(700, 600, text=text_clock,
                            font=("Arial Rounded MT Bold", 20), fill='#999999',
                            justify=CENTER, anchor=CENTER)

#Установить
btn = Button(window, text='SET AN ALARM', fg='#999999', font=('Arial Rounded MT Bold', 45), command=set_alarm_timer)
btn.place(x=250, y=800, width=500, height=100)


window.mainloop()