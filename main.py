import time
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageChops



def openfn():
    global filename
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png'), ('JPEG Files', '*.jpeg')]
    filename = filedialog.askopenfilename(title='open',filetypes=f_types)
    return filename


def open_img():
    global panel
    x = openfn()
    if x:
        img = Image.open(x).convert("RGBA")
        img = img.resize((350,350), Image.ANTIALIAS)
        img= ImageTk.PhotoImage(img)
        panel=Label(canvas, image=img)
        panel.image = img
        panel.place(relx=.5, rely=.5, anchor=CENTER)



def draw_it():
    img = filename
    my_image = Image.open(img)
    text_font = ImageFont.truetype('arial.ttf', 46)
    text_to_add = my_entry.get()
    edit_image = ImageDraw.Draw(my_image)
    edit_image.text((50,500), text= text_to_add, fill='red', font=text_font)

    my_image.save('C:/Users/Mike/Downloads/me.jpg')
    time.sleep(2)
    img_2 = Image.open('C:/Users/Mike/Downloads/me.jpg').convert("RGBA")
    img_3 = img_2.resize((350,350), Image.ANTIALIAS)
    img_4 = ImageTk.PhotoImage(img_3)
    panel.config(image=img_4)
    panel.image= img_4
    my_entry.delete(0, END)


window = Tk()
window.title('watermark creator')
window.minsize(width=700,height=700)
canvas = Canvas(width=700, height=700, bg='#e7305b')
canvas.pack(fill='both', expand=True)

the_label= Label(canvas,bg='#e7305b',fg='white', text='Please Upload the photo to which you want to add a water mark')
the_label.config(font=('Times New Roman',12, 'bold'))
the_label.place(relx=.49, rely=.12, anchor=CENTER)
upload_t = StringVar()
upload = Label(canvas, width=30,textvariable=upload_t, fg='#e7305b')
upload.place(relx=.40,rely=.2,anchor=CENTER)
upload_t.set('Your upload path here',)
upload_button= Button(canvas,width=13, text='Upload',command=open_img)
upload_button.place(relx=.65,rely=.2,anchor=CENTER)

'''cancel_button = Button(canvas, text='Cancel')
cancel_button.place(relx=.45, rely=.22)'''

my_entry = Entry(canvas, font=('arial', 14))
my_entry.place(relx=.40, rely=.8, anchor=CENTER)
my_button = Button(canvas, text='add you water-mark', font=('arial', 10), command=draw_it)
my_button.place(relx=.65, rely=.8, anchor=CENTER)
window.mainloop()



