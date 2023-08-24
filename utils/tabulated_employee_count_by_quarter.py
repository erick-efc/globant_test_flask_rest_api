import requests
from tabulate import tabulate

url = 'http://localhost:5000/api/sql/employee_count_by_quarter'

response = requests.get(url)
table = response.json()
formatted_table = tabulate(table, tablefmt='plain')
print(formatted_table)
