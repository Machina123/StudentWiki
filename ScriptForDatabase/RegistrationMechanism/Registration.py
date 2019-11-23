import pymysql
from ValidateDataToRegistration import ValidateDataToRegistration
import all_errors as error

class Registration(ValidateDataToRegistration):
    def __init__(self, email, login, passwd):
        super().__init__(email, login, passwd)
        self.prepareData()
        self.close_connection_to_db()

    def prepareData(self):
        # dodatkowe sprawdzenie czy na pewno zmienne się zapisały
        # jeżeli tak to wywołuje metodę do dodania użytkownika do bazy
        if self.getLogin() != None and self.getPassword() != None and self.getEmail() != None:
            print(self.getLogin(), self.getPassword(), self.getEmail())
            self.addToDatabase(self.getLogin(), self.getPassword(), self.getEmail())

    def addToDatabase(self, login, passwd, email):
        # generuje zapytanie i wysyła je do bazy danych
        query = f"INSERT INTO users (`id`, `login`, `email`, `password`, `user_type`) VALUES (NULL, '{login}', '{email}', '{passwd}', 'user')"
        self.cur.execute(query)
        self.con.commit()


if __name__ == '__main__':
    r = Registration('fdsfsd@student.up.krakow.pl', 'a212a', 'aa2#2FAAasda')