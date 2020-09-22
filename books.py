from db import Databank


class Books:

    def __init__(self):
        self.db = Databank()
        self.db.cursor.execute('USE library')

    def register_book(self, title, author, price):
        try:
            self.db.cursor.execute('INSERT INTO books (title, author, price) VALUES (%s, %s, %s)',
                                   (title, author, round(price, 2)))
        except Exception as error:
            print(error)
        else:
            self.db.con.commit()
            self.db.con.close()
            print('Registered Successfully!')

    def update_price_books(self, id_books, new_price):
        try:
            self.db.cursor.execute('UPDATE books SET price = %s where id_books = %s', (round(new_price, 2), id_books))
        except Exception as error:
            print(error)
        else:
            self.db.con.commit()
            self.db.con.close()
            print('Updated Successfully!')

    def delete_book(self, id_books):
        try:
            self.db.cursor.execute('DELETE FROM books where id_books = %s', (id_books,))
        except Exception as error:
            print(error)
        else:
            self.db.con.commit()
            self.db.con.close()
            print('Deleted Successfully!')

    def select_book(self, obj):
        try:
            books = []
            self.db.cursor.execute('SELECT * FROM books')
            for i in self.db.cursor.fetchall():
                books.append(i)
        except Exception as eror:
            print(eror)
        else:
            print(books)



if __name__ == '__main__':
    b = Books()
    # b.register_book()
    # b.update_price_books(1, 49.900)
    # b.register_book('Good Grief', 'Bastille', 29.90)
    # b.delete_book(3)
    b.select_book()