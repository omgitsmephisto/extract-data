import psycopg2 as pg
from psycopg2 import extras

class Database:
  def __init__(self) -> None:
    self.conn = pg.connect(
      dbname="sscp",
      user="postgres",
      password="postgres",
      host="localhost"
    )

    self.cursor = self.conn.cursor(cursor_factory=extras.DictCursor)
    self.rows = []

  def query(self, query):
    self.cursor.execute(query)
    self.rows = self.cursor.fetchall()
    # Open and closing conn in all query instances
    # [!] Not recommended for production
    self.close()
    return self.rows
  
  def close(self):
    self.cursor.close()
    self.conn.close()
  