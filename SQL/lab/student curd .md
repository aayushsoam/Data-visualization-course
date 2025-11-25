# Student CRUD CLI

Small single-file CLI app for basic student CRUD using either MySQL or SQLite.

Features
- Insert, update, delete and list students.
- Tries MySQL first (supports `mysql.connector` and `pymysql` fallbacks) then falls back to local SQLite.
- Minimal dependencies; works out-of-the-box with SQLite.

Quick links
- Source: [sql.py](sql.py)
- Key classes/functions: [`MySQLDB`](sql.py), [`PyMySQLDB`](sql.py), [`SQLiteDB`](sql.py), [`get_db`](sql.py), [`menu_loop`](sql.py), [`main`](sql.py)

Prerequisites
- Python 3.7+
- Optional (for MySQL): mysql-connector-python or pymysql
  - pip install mysql-connector-python
  - or pip install pymysql

Configuration
- Edit MySQL settings in the `MYSQL_CONFIG` dict inside [sql.py](sql.py).
- If MySQL is not available or connection fails, the app uses local SQLite file `students.db`.

Usage
1. Run the script:
```sh
python sql.py
```
2. Follow the interactive menu:
- 1 Insert student
- 2 Update student
- 3 Delete student
- 4 View all students
- 5 Exit

Notes & tips
- When using MySQL the script attempts to create the configured database and table if privileges allow.
- SQLite schema and API are implemented in [`SQLiteDB`](sql.py); MySQL wrappers are implemented by [`MySQLDB`](sql.py) and [`PyMySQLDB`](sql.py).
- To force SQLite use, decline MySQL prompt when libraries are detected.

Troubleshooting
- If mysql-connector raises auth plugin errors, the script automatically retries with the native password plugin.
- For connection issues, verify host/user/password/database in `MYSQL_CONFIG` in [sql.py](sql.py).

License
- Public domain / use as you wish.
