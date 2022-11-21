from db.run_sql import run_sql
from models.table import Table


def save(table):
    sql = "INSERT INTO tables (table_capacity) VALUES (%s) RETURNING *"

    values = [table.table_capacity]
    results = run_sql(sql, values)
    id = results[0]['id']
    table.id = id 
    return table

def select_all():
    tables = []
    sql = "SELECT * FROM tables"
    results = run_sql(sql)

    for result in results:

        table = Table(result['table_capacity'], result['id'])
        tables.append(table)
    return tables
    
def select(id):
    sql = "SELECT * FROM tables WHERE id=%s"
    results = [id]
    results = run_sql(sql, results)
# checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    if results:
        result = results[0]
 
        table = Table(result['table_capacity'],result['id'])
    return table

def delete_all():
    sql = "DELETE FROM tables"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tables WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def update(table):
    sql = "UPDATE tables SET capacity = %s WHERE id=%s"
    values = [table.table_capacity, table.id]
    run_sql(sql, values)

#  not sure whether i need to add many to many but i want to select a table and see both customer and waiter assigned to it 



