"""
Student CRUD Application (CLI)

This single-file Python app supports:
 - Insert student
 - Update student
 - Delete student
 - View all students

It attempts to use MySQL (mysql-connector). If not available or you prefer, it falls back to SQLite (local file `students.db`).

How to run:
 1. Install dependencies for MySQL (optional):
    pip install mysql-connector-python pymysql
 2. Edit the MYSQL_CONFIG below if you want to use MySQL.
 3. Run: python student_crud_app.py

Notes:
 - If the configured MySQL database doesn't exist the script will try to create it automatically (needs sufficient privileges).
 - The script will try several MySQL connection fallbacks if the default connector fails (including trying `auth_plugin='mysql_native_password'` and `pymysql`).
"""

import sys
import sqlite3
import traceback
from getpass import getpass

try:
    import mysql.connector
    MYSQL_CONNECTOR_AVAILABLE = True
except Exception:
    MYSQL_CONNECTOR_AVAILABLE = False

# pymysql is an optional fallback
try:
    import pymysql
    from pymysql.cursors import DictCursor
    PYMysql_AVAILABLE = True
except Exception:
    PYMysql_AVAILABLE = False

# ---------- Configuration ----------
MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '_______________',  # update if needed
    'database': 'college'
}

SQLITE_FILE = 'students.db'

# ---------- SQL Definitions ----------
CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INTEGER,
    branch VARCHAR(100),
    email VARCHAR(255)
)
"""

CREATE_TABLE_SQLITE = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    branch TEXT,
    email TEXT
)
"""

# ---------- MySQL Helper (mysql.connector) ----------
class MySQLDB:
    def __init__(self, config):
        self.config = config
        self.conn = None
        self.cursor = None

    def connect(self, try_native_auth=False, without_db=False):
        cfg = self.config.copy()
        if without_db:
            cfg.pop('database', None)
        if try_native_auth:
            # try connecting with explicit auth plugin
            cfg['auth_plugin'] = 'mysql_native_password'
        self.conn = mysql.connector.connect(**cfg)
        self.cursor = self.conn.cursor(dictionary=True)

    def ensure_database(self):
        # Ensure the database exists (requires privileges)
        db = self.config.get('database')
        if not db:
            return
        try:
            # connect without database to create it
            self.connect(without_db=True)
        except Exception:
            # if already connected with db, ignore
            pass
        cur = self.conn.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS `{db}`")
        self.conn.commit()
        cur.close()
        # reconnect with database
        self.conn.close()
        self.connect()

    def ensure_table(self):
        self.cursor.execute(CREATE_TABLE_SQL)
        self.conn.commit()

    def insert(self, name, age, branch, email):
        sql = "INSERT INTO students (name, age, branch, email) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (name, age, branch, email))
        self.conn.commit()
        return self.cursor.lastrowid

    def update(self, student_id, name, age, branch, email):
        sql = "UPDATE students SET name=%s, age=%s, branch=%s, email=%s WHERE id=%s"
        self.cursor.execute(sql, (name, age, branch, email, student_id))
        self.conn.commit()
        return self.cursor.rowcount

    def delete(self, student_id):
        sql = "DELETE FROM students WHERE id=%s"
        self.cursor.execute(sql, (student_id,))
        self.conn.commit()
        return self.cursor.rowcount

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def fetch_one(self, student_id):
        self.cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
        return self.cursor.fetchone()

    def close(self):
        if self.cursor:
            try:
                self.cursor.close()
            except Exception:
                pass
        if self.conn:
            try:
                self.conn.close()
            except Exception:
                pass

# ---------- PyMySQL Helper (fallback) ----------
class PyMySQLDB:
    def __init__(self, config):
        self.config = config
        self.conn = None
        self.cursor = None

    def connect(self):
        cfg = self.config.copy()
        # PyMySQL expects 'passwd' key sometimes; mysql-connector uses 'password'
        if 'password' in cfg and 'passwd' not in cfg:
            cfg['passwd'] = cfg.pop('password')
        # use DictCursor for similar behavior
        self.conn = pymysql.connect(host=cfg.get('host','localhost'), user=cfg.get('user'), password=cfg.get('passwd'), database=cfg.get('database'), cursorclass=DictCursor)
        self.cursor = self.conn.cursor()

    def ensure_database(self):
        db = self.config.get('database')
        if not db:
            return
        # connect without database
        cfg = self.config.copy()
        if 'password' in cfg and 'passwd' not in cfg:
            cfg['passwd'] = cfg.pop('password')
        conn = pymysql.connect(host=cfg.get('host','localhost'), user=cfg.get('user'), password=cfg.get('passwd'))
        cur = conn.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS `{db}`")
        conn.commit()
        cur.close()
        conn.close()
        # connect with database
        self.connect()

    def ensure_table(self):
        self.cursor.execute(CREATE_TABLE_SQL)
        self.conn.commit()

    def insert(self, name, age, branch, email):
        sql = "INSERT INTO students (name, age, branch, email) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (name, age, branch, email))
        self.conn.commit()
        return self.cursor.lastrowid

    def update(self, student_id, name, age, branch, email):
        sql = "UPDATE students SET name=%s, age=%s, branch=%s, email=%s WHERE id=%s"
        self.cursor.execute(sql, (name, age, branch, email, student_id))
        self.conn.commit()
        return self.cursor.rowcount

    def delete(self, student_id):
        sql = "DELETE FROM students WHERE id=%s"
        self.cursor.execute(sql, (student_id,))
        self.conn.commit()
        return self.cursor.rowcount

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def fetch_one(self, student_id):
        self.cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
        return self.cursor.fetchone()

    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except Exception:
            pass

# ---------- SQLite Helper ----------
class SQLiteDB:
    def __init__(self, filename):
        self.filename = filename
        self.conn = sqlite3.connect(self.filename)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def ensure_table(self):
        self.cursor.execute(CREATE_TABLE_SQLITE)
        self.conn.commit()

    def insert(self, name, age, branch, email):
        sql = "INSERT INTO students (name, age, branch, email) VALUES (?, ?, ?, ?)"
        self.cursor.execute(sql, (name, age, branch, email))
        self.conn.commit()
        return self.cursor.lastrowid

    def update(self, student_id, name, age, branch, email):
        sql = "UPDATE students SET name=?, age=?, branch=?, email=? WHERE id=?"
        self.cursor.execute(sql, (name, age, branch, email, student_id))
        self.conn.commit()
        return self.cursor.rowcount

    def delete(self, student_id):
        sql = "DELETE FROM students WHERE id=?"
        self.cursor.execute(sql, (student_id,))
        self.conn.commit()
        return self.cursor.rowcount

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM students")
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def fetch_one(self, student_id):
        self.cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
        row = self.cursor.fetchone()
        return dict(row) if row else None

    def close(self):
        self.cursor.close()
        self.conn.close()

# ---------- CLI App ----------

def input_int(prompt, default=None):
    while True:
        try:
            s = input(prompt).strip()
            if s == '' and default is not None:
                return default
            return int(s)
        except ValueError:
            print('Please enter a valid integer.')


def try_get_db_mysql(cfg):
    """Attempt to connect using different mysql strategies and return a DB wrapper on success."""
    # 1) Try mysql.connector normally
    if MYSQL_CONNECTOR_AVAILABLE:
        try:
            m = MySQLDB(cfg)
            m.connect()
            # ensure database exists and table
            m.ensure_database()
            m.ensure_table()
            print('Connected to MySQL using mysql-connector.')
            return m
        except Exception as e:
            # common issue: caching_sha2_password -> try native auth plugin
            print('mysql.connector connect failed:', e)
            try:
                m = MySQLDB(cfg)
                m.connect(try_native_auth=True)
                m.ensure_database()
                m.ensure_table()
                print('Connected to MySQL using mysql-connector with mysql_native_password auth_plugin.')
                return m
            except Exception as e2:
                print('mysql.connector with native auth failed:', e2)

    # 2) Try PyMySQL fallback
    if PYMysql_AVAILABLE:
        try:
            p = PyMySQLDB(cfg)
            p.ensure_database()
            p.ensure_table()
            print('Connected to MySQL using pymysql.')
            return p
        except Exception as e:
            print('pymysql connect failed:', e)

    # failed all
    return None


def get_db():
    use_mysql = False
    if MYSQL_CONNECTOR_AVAILABLE or PYMysql_AVAILABLE:
        resp = input('MySQL libraries available. Use MySQL? (y/N): ').strip().lower()
        use_mysql = resp == 'y'
    if use_mysql:
        cfg = MYSQL_CONFIG.copy()
        if cfg.get('password', '') == '':
            cfg['password'] = getpass('MySQL password (leave blank if none): ')

        db = try_get_db_mysql(cfg)
        if db is None:
            print('Failed to connect to MySQL with available connectors. Falling back to SQLite.')
            db = SQLiteDB(SQLITE_FILE)
    else:
        db = SQLiteDB(SQLITE_FILE)

    db.ensure_table()
    return db


def print_students(rows):
    if not rows:
        print('\nNo students found.\n')
        return
    print('\n{:<5} {:<25} {:<5} {:<15} {:<30}'.format('ID', 'Name', 'Age', 'Branch', 'Email'))
    print('-'*85)
    for r in rows:
        print('{:<5} {:<25} {:<5} {:<15} {:<30}'.format(r.get('id'), r.get('name'), r.get('age') or '', r.get('branch') or '', r.get('email') or ''))
    print()


def menu_loop(db):
    while True:
        print('''
Student CRUD Menu
1. Insert student
2. Update student
3. Delete student
4. View all students
5. Exit
''')
        choice = input('Choose an option (1-5): ').strip()
        if choice == '1':
            name = input('Name: ').strip()
            age = input_int('Age: ', default=None)
            branch = input('Branch: ').strip()
            email = input('Email: ').strip()
            new_id = db.insert(name, age, branch, email)
            print(f'Inserted student with id {new_id}\n')
        elif choice == '2':
            sid = input_int('Student ID to update: ')
            existing = db.fetch_one(sid)
            if not existing:
                print('Student not found.\n')
                continue
            print('Leave blank to keep current value.')
            name = input(f"Name [{existing.get('name')}]: ").strip() or existing.get('name')
            age_input = input(f"Age [{existing.get('age')}]: ").strip()
            age = int(age_input) if age_input != '' else existing.get('age')
            branch = input(f"Branch [{existing.get('branch')}]: ").strip() or existing.get('branch')
            email = input(f"Email [{existing.get('email')}]: ").strip() or existing.get('email')
            updated = db.update(sid, name, age, branch, email)
            print(f'Updated {updated} row(s).\n')
        elif choice == '3':
            sid = input_int('Student ID to delete: ')
            confirm = input(f'Are you sure you want to delete student id {sid}? (y/N): ').strip().lower()
            if confirm == 'y':
                deleted = db.delete(sid)
                print(f'Deleted {deleted} row(s).\n')
            else:
                print('Delete cancelled.\n')
        elif choice == '4':
            rows = db.fetch_all()
            print_students(rows)
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Try again.')


def main():
    print('Student CRUD Application')
    db = get_db()
    try:
        menu_loop(db)
    finally:
        try:
            db.close()
        except Exception:
            pass


if __name__ == '__main__':
    main()
