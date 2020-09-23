from db import Databank


class Books:

    def __init__(self):
        """Start the instance of the class"""
        self.db = Databank()
        self.db.cursor.execute('USE library')

    def register_book(self, title: str, author: str, price: float, bar_code: str, stock=0):
        try:
            if not self.verify_register(bar_code):
                self.db.cursor.execute('INSERT INTO books (title, author, price, bar_code, stock) VALUES (%s, %s, %s, '
                                       '%s, %s)', (title, author, round(price, 2), bar_code, stock))
                self.db.con.commit()
                self.db.con.close()
                print('Registered Successfully!')
            else:
                print('Book already registered!')
        except Exception as error:
            print(error)

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

    # def select_book(self, obj):
    #     try:
    #         books = []
    #         self.db.cursor.execute('SELECT * FROM books')
    #         for i in self.db.cursor.fetchall():
    #             books.append(i)
    #     except Exception as eror:
    #         print(eror)
    #     else:
    #         print(books)

    def consult_books(self, bar_code: str):
        try:
            book_data = []
            self.db.cursor.execute('SELECT * from books WHERE bar_code = %s', (bar_code,))
            for i in self.db.cursor.fetchall():
                book_data.append(i)
        except Exception as error:
            print(error)
        else:
            print(f"ID BOOK: {book_data[0][0]}\n"
                  f"TITLE: {book_data[0][1]}\n"
                  f"AUTHOR: {book_data[0][2]}\n"
                  f"PRICE: R$:{book_data[0][3]}\n"
                  f"BAR CODE: {book_data[0][4]}\n"
                  f"STOCK: {book_data[0][5]}")

    def verify_register(self, bar_code: str):
        try:
            test = []
            self.db.cursor.execute('SELECT * FROM books where bar_code = %s', (bar_code,))
            for i in self.db.cursor.fetchall():
                test.append(i)
        except Exception as error:
            print(error)
        else:
            if len(test) >= 1:
                return True
            else:
                return False


if __name__ == '__main__':
    b = Books()
    # b.register_book()
    # b.update_price_books(1, 49.900)
    # b.register_book('Good Grief', 'Bastille', 29.90)
    # b.delete_book(3)
    # b.select_book(1)
    # b.register_book("Harry Potter and the Philosopher's Stone", 'J.K Rowling', 79.90, 1234569871235)
    # b.register_book("Harry Potter and the chamber of secrets.", 'J.K. Rowling', 89.90, 9998887776662)
    # b.register_book("Harry Potter and prisoner of Azkaban.", 'J.K. Rowling', 69.90, 9998887776663)
    # b.register_book("Harry Potter and the Goblet of Fire.", 'J.K. Rowling', 49.90, 9998887776644)
    b.register_book("Harry Potter and the Order of the Phoenix.", 'J.K. Rowling', 59.90, 9998887744662)
