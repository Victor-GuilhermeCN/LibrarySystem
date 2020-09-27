from db import Databank


class Books:

    def __init__(self):
        """Start the instance of the class"""
        self.db = Databank()
        self.db.connection()
        # self.db.cursor.execute('USE library')

    def register_book(self, title: str, author: str, price: float, barcode: str, stock=0):
        """This method register the book in the books table, but before checks if the books is already registered.
        I decided to use the barcode in data string, because I can use the both bar code parameters.
        And the stock is defined in 0, because if the user doesn't pass the stock, the quantity ir already set to 0
        :param title: str
        :param author: str
        :param price:float
        :param barcode: str
        :param stock:str """
        try:
            if not self.verify_register(barcode):
                self.db.cursor.execute('INSERT INTO books (title, author, price, bar_code, stock) VALUES (%s, %s, %s, '
                                       '%s, %s)', (title, author, round(price, 2), barcode, stock))
                self.db.con.commit()
                self.db.con.close()
                print('Registered Successfully!')
            else:
                print('Book already registered!')
        except Exception as error:
            print(error)

    def update_price_books(self, barcode, new_price):
        """This method update the price of the books, by the barcode.
        :param barcode:str
        :param new_price: float"""
        try:
            self.db.cursor.execute('UPDATE books SET price = %s where id_books = %s', (round(new_price, 2), barcode))
        except Exception as error:
            print(error)
        else:
            self.db.con.commit()
            self.db.con.close()
            print('Updated Successfully!')

    def delete_book(self, barcode):
        """This method deleted books already registered in the database, by the barcode.
        :param barcode: str"""
        try:
            self.db.cursor.execute('DELETE FROM books where id_books = %s', (barcode,))
        except Exception as error:
            print(error)
        else:
            self.db.con.commit()
            self.db.con.close()
            print('Deleted Successfully!')

    def consult_books(self, bar_code: str):
        """This method return the specifications of the books, consulting the database by barcode"""
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

    def verify_register(self, barcode: str):
        """This method checks if the books is already registered in the database, by barcode.
        :param barcode: str"""
        try:
            test = []
            self.db.cursor.execute(f'SELECT * FROM books where bar_code = {barcode}')
            for i in self.db.cursor.fetchall():
                test.append(i)
        except Exception as error:
            print(error)
        else:
            if len(test) >= 1:
                return True
            else:
                return False

    def consult(self, attribute):
        data = []
        try:
            self.db.cursor.execute(f'SELECT {attribute} from books')
            for i in self.db.cursor.fetchall():
               data.append(i)
        except Exception as eror:
            print(eror)
        else:
            print(data)


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
    # b.register_book("Harry Potter and the Order of the Phoenix.", 'J.K. Rowling', 59.90, 9998887744662)
    b.consult_books(1234569871235)