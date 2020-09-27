from db import Databank


class Client:

    def __init__(self, cpf: str, name: str, last_name: str, birth_date: str, password: str):
        """This method starts the class.
        :param cpf:str
        :param name:str
        :param last_name: str
        :param birth_date: str
        :param password: str"""
        self.db = Databank()
        self.db.cursor.execute('USE library')
        self.cpf = cpf
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.password = password

    def format_age(self):
        """ This method transforms the dates to the MYSQL default YYYYMMDD
        :param: birth_date:str"""
        birth_date = self.birth_date.splitlines()
        bday = [birth_date[0][0], birth_date[0][1]]
        day = [''.join(bday)]
        monthday = [birth_date[0][2], birth_date[0][3]]
        month = [''.join(monthday)]
        yearday = [birth_date[0][4], birth_date[0][5], birth_date[0][6], birth_date[0][7]]
        year = [''.join(yearday)]
        conclusion = f'{year[0]}{month[0]}{day[0]}'
        return conclusion

    def get_age(self):
        """This method return the age of all client registered in the databank, without filter or condition. It's still
        in the improvement phase."""
        try:
            age = []
            self.db.cursor.execute(f'SELECT YEAR(FROM_DAYS(TO_DAYS(NOW())-TO_DAYS(client.birth_date))) AS age FROM '
                                   f'client')
            for i in self.db.cursor.fetchall():
                age.append(i)
        except Exception as error:
            print(error)
        else:
            for list in age:
                print(*list)

    def verify(self, cpf: str):
        """This method checks if the user is already registered in the system
        :param cpf:str"""
        try:
            verification = []
            self.db.cursor.execute('SELECT * from client where cpf = %s', (cpf,))
            for i in self.db.cursor.fetchall():
                verification.append(i)
        except Exception as erro:
            print(erro)
        else:
            if len(verification) >= 1:
                return True
            else:
                return False

    def client_register(self):
        """This method register the client using the data passed in the class instance, but before verify if the client
         is already registered!"""
        try:
            if not self.verify(self.cpf):
                self.db.cursor.execute('INSERT INTO client (cpf, name, last_name, birth_date, password) values (%s, %s,'
                                       ' %s, %s, %s)', (self.cpf, self.name, self.last_name, self.format_age(),
                                                        self.password))

                self.db.con.commit()
                self.db.con.close()
                print('Registered successfully!')
            else:
                print('Client already registered!')
        except Exception as error:
            print(error)

    def client_update(self, cpf: str, name: str):
        """This method update the client name in the database, using cpf as condition.
        :param cpf:str
        :param name:str"""
        try:
            self.db.cursor.execute(f'UPDATE client SET name = %s where cpf = {cpf}', (name,))
            self.db.con.commit()
            self.db.con.close()
            print('Updated Successfully!')
        except Exception as error:
            print(error)

    def delete_client(self, cpf: str):
        """This method delete the client account in the database, using cpf as parameter.
        :param cpf:str"""
        try:
            self.db.cursor.execute(f'DELETE from client where cpf = {cpf}')
            self.db.con.commit()
            self.db.con.close()
            print('Deleted Successfully!')
        except Exception as error:
            print(error)


if __name__ == '__main__':
    c = Client('11373410732', 'Victor', 'Guilherme da Silva', '25071996', 'abc123')
    # c.client_register()
    # c.client_update('11373410732', 'Vktron2')
    # c.delete_client(11373410732)
    c.get_age()