from db.run_sql import run_sql
from models.table import Table
from models.customer import Customer
from models.waiter import Waiter

import repositories.customer_repository as customer_repository
import repositories.waiter_repository as waiter_repository

def save(table):
    sql = "INSERT INTO tables (capacity, time_slot, customer_id, waiter_id) VALUES (%s,%s,%s,%s) RETURNING *"

    values = [table.capacity,table.time_slot, table.customer_id.id, table.waiter_id.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    table.id = id 
    return table

def select_all():
    tables = []
    sql = "SELECT * FROM tables"
    results = run_sql(sql)

    for result in results:
        customer = customer_repository.select(result['customer_id'])
        waiter = waiter_repository.select(result['waiter_id'])
        table = Table(result['capacity'], result["time_slot"], customer, waiter, result['id'])
        tables.append(table)
    return tables
    
def select(id):
    sql = "SELECT * FROM tables WHERE id=%s"
    results = [id]
    results = run_sql(sql, results)
# checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    if results:
        result = results[0]
        customer = customer_repository.select(result['customer_id'])
        waiter = waiter_repository.select(result['waiter_id'])
        table = Table(result['capacity'],result["time_slot"], customer, waiter, result['id'])
    return table

def delete_all():
    sql = "DELETE FROM tables"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tables WHERE id=%s"
    values = [id]
    run_sql(sql, values)

def update(table):
    sql = "UPDATE tables SET (capacity, time_slot,customer_id, waiter_id) = (%s,%s,%s,%s) WHERE id=%s"
    values = [table.capacity, table.time_slot, table.customer_id.id, table.waiter_id.id, table.id]
    run_sql(sql, values)

#  not sure whether i need to add many to many but i want to select a table and see both customer and waiter assigned to it 

