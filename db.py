import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS labour(
            id Integer Primary Key,
            name text,
            age text,
            dob text,
            email text,
            gender text,
            contact text,
            salary text,
            schemes text,
            worklocation text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, age, dob, email, gender, contact, salary, schemes, worklocation, address):
        self.cur.execute("insert into labour values (NULL,?,?,?,?,?,?,?,?,?,?)",
                         (name, age, dob, email, gender, contact, salary, schemes, worklocation, address))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from labour")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from labour where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, age, dob, email, gender, contact, salary, schemes, worklocation, address):
        self.cur.execute(
            "update labour set name=?, age=?, dob=?, email=?, gender=?, contact=?, salary=?, schemes=?, worklocation=?, address=? where id=?",
            (name, age, dob, email, gender, contact, salary, schemes, worklocation, address, id))
        self.con.commit()
