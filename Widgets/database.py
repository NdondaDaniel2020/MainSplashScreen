import sqlite3

class database():

    def __init__(self, name='banco'):
        if '.db' in name:
            self.name = name
        else:
            self.name = name+'.db'

    def connect_database(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection_database(self):
        try:
            self.connection.commit() ## commit salva os dados no banco
            self.connection.close()
        except:
            print('nemum banco conectado')

    def create_table(self, nametable):
        cursor = self.connection.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {nametable}(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
            nome varchar(20) NOT NULL UNIQUE,
            password varchar(30) NOT NULL,
            admin TEXT CHECK( admin IN ('T','F')) NOT NULL DEFAULT 'F'
            ) ;
        """)

    def insert_into(self, nametable, name, passw, user=False):

        if user:
            user = 'T'
        else:
            user = 'F'

        cursor = self.connection.cursor()
        try:
            cursor.execute(f"""
        INSERT INTO {nametable}(nome, password, admin) VALUES('{name}', '{passw}', '{user}');
        """)
        except:
            print("nao consegui enviar os dados")

    def select_from(self, nametable):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM {nametable} ORDER BY nome")
            user = cursor.fetchall()
            return user
        except:
            print('error select')

    def __str__(self):
        return 'Class para criares o teu banco de dados'




