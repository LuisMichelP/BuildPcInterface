import sqlite3
from tkinter import *
from tkinter import ttk
class pc:
    
    def __init__(self, motherboard, processor, graphics, randomemory, storage, price):
        self.motherboard = motherboard
        self.processor = processor
        self.graphics = graphics
        self.ram = randomemory
        self.storage = storage
        self.price = price
    
    def save(self):
        with sqlite3.connect('archi.db') as db:
            cursor = db.cursor()
        
        cursor.execute('''INSERT INTO userpc(motherboard, processor, graphics, ram, storage, price) VALUES(?,?,?,?,?,?)''',
                       (self.motherboard, self.processor, self.graphics, self.ram,self.storage, self.price))
        db.commit()
        
