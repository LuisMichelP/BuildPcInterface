from tkinter import *
from tkinter import messagebox
import sqlite3
from objects import *

computertest = ['','','','','',0]
prices = [0,0,0,0,0]

with sqlite3.connect('archi.db') as db:
    cursor = db.cursor()

def query(category, specification):
    cpu = ['LGA','AM4','AM3']
    gpu = ['ATX','ITX']
    ram = ['DDR4','DDR5','DDR3']
    if computertest[0] != '' and category == 'cpu':
        print('test')
        for row in cpu:
            if row in computertest[0]:
                cursor.execute('SELECT product_name,description FROM components WHERE category=? AND description LIKE ?',[category, f'%{row}%{specification}%'])
                results = cursor.fetchall()
                return results
    if computertest[0] != '' and category == 'gpu':
        for row in gpu:
            if row in computertest[0]:
                cursor.execute('SELECT product_name,description FROM components WHERE category=? AND description LIKE ?',[category, f'%{row}%'+specification+'%'])
                results = cursor.fetchall()
                return results
    if computertest[0] != '' and category == 'ram':
        for row in ram:
            if row in computertest[0]:
                cursor.execute('SELECT product_name,description FROM components WHERE category=? AND description LIKE ?',[category, f'%{row}%'+specification+'%'])
                results = cursor.fetchall()
                return results
    else:
        cursor.execute('SELECT product_name,description FROM components WHERE category=? AND description LIKE ?',[category, '%'+specification+'%'])
        results = cursor.fetchall()
        return results

def show_full_description(product_brand,product_description):
    cursor.execute('SELECT product_name,description,price FROM components WHERE product_name=? AND description=?',[product_brand,product_description])
    product = cursor.fetchall()
    messagebox.showinfo(message=f'Brand: {product[0][0]}\nDescription: {product[0][1]}\nPrice: {product[0][2]:.2f}',title='Description')

def addtopc(product_description):
    cursor.execute('SELECT description, price,category FROM components WHERE description=?',[product_description])
    product = cursor.fetchall()
    category = product[0][2]
    price = product[0][1]
    product= (product[0][0])

    if category == 'motherboard':
        computertest[0]=product
        prices[0] = price
    elif category == 'cpu':
        computertest[1]=product
        prices[1] = price
    elif category == 'gpu':
        computertest[2]=product
        prices[2] = price
    elif category == 'ram':
        computertest[3]=product
        prices[3] = price
    else:
        #category == storage
        computertest[4]=product
        prices[4] = price
    computertest[5] = sum(prices)

    return computertest

def saveto(computertest):
    messagebox.showinfo(message='Your PC was succesfully uploaded!', title="Saved!")
    user = pc(computertest[0],computertest[1],computertest[2], computertest[4],computertest[3],computertest[5])
    user.save()
