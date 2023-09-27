import sqlite3

CONN = sqlite3.connect("stats.db")
CURSOR = CONN.cursor()
