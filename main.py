from tkinter import *
from tkinter import ttk
from functions import query, show_full_description, addtopc, saveto, computertest
from objects import pc

#Window
window = Tk()
window.title('Build Your own PC')
window.geometry('950x550')
window.config(background='#418DB6')

#buttons functions
def getquery():
    parts.delete(*parts.get_children())
    category = category_drop.get()
    spec = specification.get()
    
    results = query(category.lower(),spec)
    for row in results:
        parts.insert("", "end", values=(row[0],row[1]))
    specification.delete(0,END)

def viewmore():
    selected = parts.selection()[0]
    show_full_description(parts.item(selected)['values'][0],parts.item(selected)['values'][1])

def testpc():
    selected = parts.selection()[0]
    computertest = addtopc(parts.item(selected)['values'][1])
    yourpc = Label(text=f'Your PC: \nMotherboard: {computertest[0][:20]} \nCPU: {computertest[1][:20]} \nGraphics: {computertest[2][:20]} \nRAM: {computertest[3][:20]} \nStorage: {computertest[4][:20]}\n\nPrice: ${computertest[5]:.2f}')
    yourpc.place(x=700, y=120)
    yourpc.config(font=('Helvetica bold',10), bg='#418DB6', fg='black')
    return computertest

def save():
    saveto(computertest)

#Labels
Intro = Label(text='Welcome to our PCBuilder')
Intro.place(x=20,y=25)
Intro.config(font=('Helvatical bold',20), bg='#418DB6', fg='black')

#Inputs
category_drop = StringVar(window)
category_drop.set("Category")
categorylist = OptionMenu(window, category_drop, 'CPU', 'Motherboard', 'RAM', 'Storage', 'GPU')
categorylist.place(x=20, y=87, height=25)
categorylist.config(bg='#0A3E5B', fg='white')

specification = Entry(text='')
specification.place(x= 140, y=87, height= 25)

#query table
cols = ('Brand', 'Description')
parts = ttk.Treeview(window, columns=cols, show='headings')
for col in cols:
    parts.heading(col, text=col)
parts.place(x=20,y=120, height=400)
parts.column("Brand", minwidth=0, width=100, stretch=NO)
parts.column("Description", minwidth=0, width=500, stretch=NO)

#buttons
search = Button(text='Search',command=getquery, bg='#0A3E5B', fg='white').place(x=270, y=87)
search

more = Button(text='View more',command=viewmore, bg='#0A3E5B', fg='white').place(x=555,y=87)

add = Button(text='Add to the pc',command=testpc, bg='#0A3E5B', fg='white').place(x=650,y=87)

savebutton = Button(text='Save to', command=save, bg='#0A3E5B', fg='white').place ( x=740, y=280, width=100, height=30)

window.mainloop()