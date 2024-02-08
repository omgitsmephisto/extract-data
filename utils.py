def get_excel_rows_in_postgres_format(excel, emails):
  for line in excel.values:
    email = line[1]
    emails.append("'" + email + "'")
  return emails