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

    def table_books(self):
        try:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS books (id_books int(10) PRIMARY KEY AUTO_INCREMENT, title '
                                'varchar(255) not null, author varchar(255) not null, price decimal(10,2), bar_code '
                                'varchar(13), stock int(10))')
        except Exception as error:
            print(error)
        else:
            print('Table Created successfully!')
            
    def table_client(self):
        try:
            self.cursor.execute('USE library')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS client (cpf varchar(11) PRIMARY KEY, name varchar(255) '
                                'not null, last_name varchar(255) not null, birth_date date, password varchar(16))')
        except Warning as error:
            print(error)
        else:
            print('Created Successfully')

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
        self.table_books()
        self.table_client()


if __name__ == '__main__':
    db = Databank()
    # db.create_db()
    # db.create_table()
    # db.verify_connection()
    db.create_db()
    # db.table_client()
