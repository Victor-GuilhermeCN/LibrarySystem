from db import Databank

class Books:

    def __init__(self, title, author, price):
        self.db = Databank()
        self.title = title
        self.author = author
        self.price = price


    def register_book(self):
        try:
            self.db.cursor.execute('INSERT INTO books (title, author, price) VALUES (%s, %s, %s)',
                                   (self.title, self.author, self.price))
        except Exception as error:
            print(error)
        else:
            self.db.con.commit()
            self.db.con.close()
            print('Registered Successfully!')
