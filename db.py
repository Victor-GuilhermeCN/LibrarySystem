import pymysql


class Databank:

    def __init__(self):
        self.con = pymysql.connect(user='root', passwd='')
        self.cursor = self.con.cursor()

    def database(self):
        try:
            self.cursor.execute('CREATE DATABASE library')
        except Exception as error:
            print(error)
        else:
            self.cursor.execute('USE library')
            print('Database created successfully!')

    def create_table(self):
        try:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS books (id_books int(10) PRIMARY KEY AUTO_INCREMENT, title '
                                'varchar(255) not null, author varchar(255) not null, price decimal(10,2))')
        except Exception as error:
            print(error)
        else:
            print('Table Created successfully!')

    def verify_connection(self):
        try:
            self.cursor.execute('USE library')
        except Exception as error:
            print('Error connection!')
            print(error)
        else:
            print('Connection successfully!')

    def create_db(self):
        self.database()
        self.create_table()


if __name__ == '__main__':
    db = Databank()
    # db.create_db()
    # db.create_table()
    # db.verify_connection()
    db.create_db()