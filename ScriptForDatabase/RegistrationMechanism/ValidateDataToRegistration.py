import pymysql
import re
import hashlib
import all_errors as error

class ValidateDataToRegistration(object):
    def __init__(self, email, login, passwd):
        self.email = email
        self.login = login
        self.passwd = passwd
        self.con = None
        self.cur = None
        self.connect_to_db()
        self.check_email()
        self.check_login()
        self.check_passwd()
        # self.close_connection_to_db()

    def connect_to_db(self):
        # połączenie z BD, zwraca wyjątek jeżeli nie udało się połączyć z BD
        # zakładam że 'BD' będzie na osobnym serwerze (ew. docker)
        try:
            self.con = pymysql.Connect(host='127.0.0.1', user='root', unix_socket='', passwd='', db='mysql')
            self.cur = self.con.cursor()
            self.cur.execute("USE studentup")
        except:
            raise error.ConnectionRefused("Brak połączenia z serwerem")

    def close_connection_to_db(self):
        self.cur.close()

    def check_email(self):
        # metoda do sprawdzania czy email jest poprawny
        # jeżeli email nie należy do domeny uczelnianej
        # zwraca wyjątek
        tmp = self.email[self.email.index('@') + 1:]
        if(tmp != 'student.up.krakow.pl'):
            self.email = None
            raise error.BadEmail("Podany email nie jest z domeny uczelnianej")

    def check_login(self):
        # sprawdza czy podany przez użytkownika login jest w bazie
        # jeżeli jest zwraca wyjątek
        query = 'SELECT login FROM users WHERE login = "' + self.login + '"'
        if(self.cur.execute(query)):
            self.login = None
            raise error.ExistingUser("Podany login istnieje już w bazie")

    def check_passwd(self):
        # sprawdza czy hasło spełnia wymogi bezpieczeństwa,
        # jeżeli tak zostaje zahashowane, w przeciwnym wypadku zwraca wyjątek
        wzorzec = "^(?=.*\d)(?=.*[a-z])(?=.*[\!\@\#\$\%\^\&\*\(\)\_\+\-\=])(?=.*[A-Z])(?!.*\s).{8,}$"
        test = re.search(wzorzec, self.passwd)
        if(test):
            hasher = hashlib.sha256()
            hasher.update(bytes(self.passwd, encoding='utf-8'))
            self.passwd = hasher.hexdigest()
        else:
            self.passwd = None
            raise error.NotEnoughtPassword("Podane hasło nie spełnia wymogów bezpieczeństwa")

    def getLogin(self):
        return self.login

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.passwd