import sqlite3

class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table(self):
        sql = """
        CREATE TABLE Kino(
            name TEXT NOT NULL,
            about TEXT NOT NULL,
            pic_link TEXT NOT NULL,
            down_code TEXT NOT NULL
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def mk_vd(self, name: str, about: str, pic_link: str, down_code : str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Kino(name, about, pic_link, down_code) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(name, about, pic_link,down_code), commit=True)
    def get_vd(self):
        x = self.execute("""SELECT * FROM Kino""",fetchall=True)
        print(x)
        return x
    def cnt_vd(self):
        x = self.execute("SELECT COUNT(*) FROM Kino;", fetchone=True)
        print(x)
        return x
        



def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")