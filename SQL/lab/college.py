import pymysql
from pymysql.err import MySQLError as Error
from datetime import datetime
import sys

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "@@y$o@@m",
    "database": "student"
}

# ---------- DB Conn ----------
def get_conn():
    return pymysql.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"],
        cursorclass=pymysql.cursors.Cursor
    )

# ---------- Create Tables ----------
def ensure_tables():
    create_course = """
    CREATE TABLE IF NOT EXISTS Course (
      courseid VARCHAR(50) PRIMARY KEY,
      coursename VARCHAR(255) NOT NULL,
      duration VARCHAR(100),
      min_enrollment INT,
      max_enrollment INT
    );
    """

    create_faculty = """
    CREATE TABLE IF NOT EXISTS Faculty (
      facultyid VARCHAR(50) PRIMARY KEY,
      facultyname VARCHAR(255) NOT NULL,
      age INT,
      dob DATE,
      qualification VARCHAR(255)
    );
    """

    create_module = """
    CREATE TABLE IF NOT EXISTS Module (
      moduleid VARCHAR(50) PRIMARY KEY,
      modulename VARCHAR(255) NOT NULL,
      courseid VARCHAR(50),
      facultyid VARCHAR(50),
      duration VARCHAR(100),
      FOREIGN KEY (courseid) REFERENCES Course(courseid) ON DELETE SET NULL,
      FOREIGN KEY (facultyid) REFERENCES Faculty(facultyid) ON DELETE SET NULL
    );
    """

    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(create_course)
        cur.execute(create_faculty)
        cur.execute(create_module)
        conn.commit()
    finally:
        cur.close()
        conn.close()

# ---------- COURSE ----------
def insert_course(courseid, coursename, duration, min_e, max_e):
    sql = """INSERT INTO Course (courseid, coursename, duration, min_enrollment, max_enrollment)
             VALUES (%s, %s, %s, %s, %s)"""
    conn = get_conn(); cur = conn.cursor()
    try:
        cur.execute(sql, (courseid, coursename, duration, min_e, max_e))
        conn.commit()
    finally:
        cur.close(); conn.close()

def fetch_all_courses():
    conn = get_conn(); cur = conn.cursor()
    cur.execute("SELECT * FROM Course")
    rows = cur.fetchall()
    cur.close(); conn.close()
    return rows

def update_course(courseid, **fields):
    if not fields: 
        return 0
    set_clause = ", ".join(f"{k}=%s" for k in fields.keys())
    sql = f"UPDATE Course SET {set_clause} WHERE courseid=%s"
    params = tuple(fields.values()) + (courseid,)
    conn = get_conn(); cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    rc = cur.rowcount
    cur.close(); conn.close()
    return rc

# ---------- FACULTY ----------
def insert_faculty(fid, name, age, dob, qual):
    sql = """INSERT INTO Faculty VALUES (%s, %s, %s, %s, %s)"""
    conn = get_conn(); cur = conn.cursor()
    cur.execute(sql, (fid, name, age, dob, qual))
    conn.commit()
    cur.close(); conn.close()

def fetch_all_faculty():
    conn = get_conn(); cur = conn.cursor()
    cur.execute("SELECT * FROM Faculty")
    rows = cur.fetchall()
    cur.close(); conn.close()
    return rows

def update_faculty(fid, **fields):
    if not fields: return 0
    set_clause = ", ".join(f"{k}=%s" for k in fields.keys())
    sql = f"UPDATE Faculty SET {set_clause} WHERE facultyid=%s"
    params = tuple(fields.values()) + (fid,)
    conn = get_conn(); cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    rc = cur.rowcount
    cur.close(); conn.close()
    return rc

# ---------- MODULE ----------
def insert_module(mid, name, cid, fid, duration):
    sql = "INSERT INTO Module VALUES (%s, %s, %s, %s, %s)"
    conn = get_conn(); cur = conn.cursor()
    cur.execute(sql, (mid, name, cid, fid, duration))
    conn.commit()
    cur.close(); conn.close()

def fetch_all_modules():
    sql = """
    SELECT m.moduleid, m.modulename, m.courseid, c.coursename,
           m.facultyid, f.facultyname, m.duration
    FROM Module m
    LEFT JOIN Course c ON m.courseid = c.courseid
    LEFT JOIN Faculty f ON m.facultyid = f.facultyid
    """
    conn = get_conn(); cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close(); conn.close()
    return rows

# ---------- Helpers ----------
def input_nonempty(msg):
    v = input(msg).strip()
    while not v:
        v = input(msg).strip()
    return v

def print_table(headers, rows):
    print("-" * 80)
    print(" | ".join(headers))
    print("-" * 80)
    for r in rows:
        print(" | ".join(str(x) if x is not None else "" for x in r))
    print("-" * 80)

# ---------- Menus ----------
def course_menu():
    while True:
        print("\nCourse Menu: 1) Add  2) List  3) Update  0) Back")
        ch = input("Choice: ").strip()

        if ch == "1":
            cid = input_nonempty("courseid: ")
            name = input_nonempty("coursename: ")
            dur = input("duration: ").strip() or None
            min_e = input("min_enroll: ").strip() or None
            max_e = input("max_enroll: ").strip() or None
            insert_course(cid, name, dur, min_e, max_e)
            print("Inserted.")

        elif ch == "2":
            rows = fetch_all_courses()
            print_table(["courseid","name","duration","min","max"], rows)

        elif ch == "3":
            cid = input("courseid to update: ").strip()
            cname = input("new name: ").strip()
            dur = input("new duration: ").strip()
            fields = {}
            if cname: fields["coursename"] = cname
            if dur: fields["duration"] = dur
            print("Rows updated:", update_course(cid, **fields))

        elif ch == "0":
            break

def faculty_menu():
    while True:
        print("\nFaculty Menu: 1) Add  2) List  3) Update  0) Back")
        ch = input("Choice: ").strip()

        if ch == "1":
            fid = input_nonempty("facultyid: ")
            name = input_nonempty("facultyname: ")
            age = input("age: ").strip() or None
            dob = input("dob YYYY-MM-DD: ").strip() or None
            qual = input("qualification: ").strip() or None
            insert_faculty(fid, name, age, dob, qual)
            print("Inserted.")

        elif ch == "2":
            rows = fetch_all_faculty()
            print_table(["facultyid","name","age","dob","qual"], rows)

        elif ch == "3":
            fid = input("facultyid: ").strip()
            fname = input("new name: ").strip()
            fields = {}
            if fname: fields["facultyname"] = fname
            print("Rows updated:", update_faculty(fid, **fields))

        elif ch == "0":
            break

def module_menu():
    while True:
        print("\nModule Menu: 1) Add  2) List  3) Update  0) Back")
        ch = input("Choice: ").strip()

        if ch == "1":
            mid = input_nonempty("moduleid: ")
            name = input_nonempty("modulename: ")
            cid = input("courseid: ").strip() or None
            fid = input("facultyid: ").strip() or None
            dur = input("duration: ").strip() or None
            insert_module(mid, name, cid, fid, dur)
            print("Inserted.")

        elif ch == "2":
            rows = fetch_all_modules()
            print_table(["mid","name","cid","coursename","fid","faculty","dur"], rows)

        elif ch == "3":
            print("Update feature can be added here")

        elif ch == "0":
            break

# ---------- Main ----------
def main():
    try:
        ensure_tables()
    except Error as e:
        print("Database error:", e)
        sys.exit()

    while True:
        print("\nMain Menu: 1) Course  2) Faculty  3) Module  0) Exit")
        ch = input("Choice: ").strip()

        if ch == "1":
            course_menu()
        elif ch == "2":
            faculty_menu()
        elif ch == "3":
            module_menu()
        elif ch == "0":
            break

if __name__ == "__main__":
    main()
