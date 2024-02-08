import pandas as pd

from database import Database
from utils import get_excel_rows_in_postgres_format

excel = pd.read_excel('sheets.xlsx')
db = Database()

emails = []
db_emails = []

emails = get_excel_rows_in_postgres_format(excel, emails)
rows = db.query(f"SELECT email FROM users u WHERE u.email IN ({', '.join(emails)})")

for row in rows:
  db_emails.append(row[0])

for index, email in enumerate(emails):
  for db_email in db_emails:
    if (email.replace("'", "") == db_email):
      emails.pop(index)

print(emails)
print(rows)